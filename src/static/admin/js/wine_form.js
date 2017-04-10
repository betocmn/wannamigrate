
var $attr,
wine_form = {

    // Internal attributes to be used on this module
    attributes: {
        uploading: false,
        current_photos: {},
        blend_wine_type_ids: [],
        upload_url: '',
        pairings_url: '',
        wine_preservatives_formset: '',
        wine_photos: '',
        wine_blend_wine_types_formset: '',
        selectize: {fruits: {}, food: {}, moods: {}, flavours: {}, seasons: {}, tastes: {}}
    },

    // Constructor
    init: function(args) {
        $attr = this.attributes
        $attr.current_photos = args.current_photos;
        $attr.blend_wine_type_ids = args.blend_wine_type_ids;
        $attr.upload_url = args.upload_url;
        $attr.pairings_url = args.pairings_url;
        $attr.wine_preservatives_formset = args.wine_preservatives_formset;
        $attr.wine_blend_wine_types_formset = args.wine_blend_wine_types_formset;
        $attr.wine_photos = args.wine_photos;
        this.setup_elements();
        this.setup_events();
        this.reorder_fieldsets();
        this.toggle_blend_wine_types_container($('#id_wine_type').val());
    },

    // Form elements using 3rd party formatting
    setup_elements: function() {

        // Form Masks
        $("#id_weight, #id_height, #id_length, #id_width, #id_gst_tax_price, #id_wet_tax_price, " +
            "#id_oak_aged_years," +
            "#id_alcohol_percentage, #id_selling_price, #id_buying_price").mask('###0.00', {reverse: true});

        // Validation for low values
        $('#id_buying_price').blur(function () {
            if($(this).val() != '' && $(this).val() < 5){
                alert("You've entered a low buying price, make sure it's correct!")
            }
        });
        $('#id_selling_price').blur(function () {
            if($(this).val() != '' && $(this).val() != 23){
                alert("You've entered a selling price other than $23, make sure it's correct!")
            }
        });

        // Alternative select box (using selectize)
        var create_select_fields = "#id_wine_body, #id_wine_tannin, #id_wine_supplier, " +
            "#id_wine_acidity, #id_wine_sweetness, #id_wine_bottle_design, #id_fruit";
        var simple_select_fields = "#id_wine_type, #id_wine_maker, #id_wine_cellar_period";
        $(create_select_fields).selectize({create: true, sortField: 'text'});
        $(simple_select_fields).selectize({create: false,sortField: 'text'});

        // Alternative multiple select box (using selectize)
        $attr.selectize.fruits = $('#id_fruits').selectize({delimiter: ',', persist: false, create: true});
        $attr.selectize.food = $('#id_food').selectize({delimiter: ',', persist: false, create: true});
        $attr.selectize.moods= $('#id_moods').selectize({delimiter: ',', persist: false, create: true});
        $attr.selectize.flavours = $('#id_flavours').selectize({delimiter: ',', persist: false, create: true});
        $attr.selectize.seasons = $('#id_seasons').selectize({delimiter: ',', persist: false, create: false});
        $attr.selectize.tastes = $('#id_tastes').selectize({delimiter: ',', persist: false, create: true});
        $('#id_wine_production_methods').selectize({delimiter: ',', persist: false, create: true});

        // Django Formset Generation
        $( '#main_form div.preservatives' ).formset({
            formCssClass: 'dynamic-preservatives-form',
            prefix: $attr.wine_preservatives_formset,
            addCssClass: 'btn btn-default ' + $attr.wine_preservatives_formset,
            addText: 'add another',
            deleteText: 'delete'
        });
        $( '#main_form div.blend_wine_types' ).formset({
            formCssClass: 'dynamic-blend-wine-types-form',
            prefix: $attr.wine_blend_wine_types_formset,
            addCssClass: 'btn btn-default ' + $attr.wine_blend_wine_types_formset,
            addText: 'add another',
            deleteText: 'delete'
        });

        // Makes fieldsets expandable (collapsible)
        new jQueryCollapse($(".fieldset"), {
            query: 'div.panel-heading'
        });
        $("#product-information-fieldset div.panel-heading a").trigger("open");
        $("#photos-fieldset div.panel-heading a").trigger("open");
        $("#wine-identification-fieldset div.panel-heading a").trigger("open");

        // Setup upload form (using DropzoneJs)
        wine_form.setup_upload();

    },

    // Creates checkbox for cover photo (primary)
    create_cover_checkbox: function(file, response) {
        var cover = $('<div>', {"class":"dz-cover"})
        $('<span>').html('cover:').appendTo(cover);
        var checkbox = $('<input>', {
            type: "radio",
            "name": "cover",
            "value": response.product_photo_id,
            "id": file.name.toLowerCase().replace(/[^a-zA-Z0-9]/g,'-')
        });
        checkbox.on('change', function () {
            wine_form.set_as_cover($(this).val());
        });
        if(response.is_primary){
            checkbox.prop("checked", true);
        }
        checkbox.appendTo(cover);
        cover.appendTo(file.previewTemplate);
        file.product_photo_id = response.product_photo_id;
    },

    // Sets a photo as the cover one (primary)
    set_as_cover: function(product_photo_id) {
        $.post($attr.upload_url, {primary_id: product_photo_id}, function(data, status){
            //alert("Set as primary - Data: " + data + "\nStatus: " + status);
        });
    },

    // Only displays the blend wine types formset when a blend type was selected
    toggle_blend_wine_types_container: function(wine_type_id) {
        var display = false;
        if(wine_type_id){
            if(jQuery.inArray(parseInt(wine_type_id), $attr.blend_wine_type_ids) != -1){
                display = true;
            }
        }
        $("#blend-wine-types-fieldset").toggle(display);
    },

    // Set default wine pairings
    set_default_pairings: function(wine_type_id) {
        if(wine_type_id){
            var url = $attr.pairings_url;
            var post_data = {wine_type_id: wine_type_id};
            $.post(url, post_data, function(data, status){
                if(data.status == 'success'){
                    $attr.selectize.fruits[0].selectize.setValue(data.fruits);
                    $attr.selectize.food[0].selectize.setValue(data.food);
                    $attr.selectize.moods[0].selectize.setValue(data.moods);
                    $attr.selectize.seasons[0].selectize.setValue(data.seasons);
                    $attr.selectize.flavours[0].selectize.setValue(data.flavours);
                    $attr.selectize.tastes[0].selectize.setValue(data.tastes);
                }
            });
        }

    },

    // Change the position of some fieldsets on the form
    reorder_fieldsets: function() {
        $("#blend-wine-types-fieldset").insertAfter("#wine-identification-fieldset");
        $("#seo-fieldset").insertAfter("#preservatives-fieldset");

    },

    // Jquery Events
    setup_events: function() {

        // Submits form with JS (it was needed to keep the dropzone as a separate form)
        $( "#main_form_submit" ).click( function() {
            if($attr.uploading){
                alert( 'Please wait for uploads to finish and try again');
                return false;
            }
            $("#main_form").submit();
        });

        // Actions when changing the wine type
        $("#id_wine_type").change(function(){
            var wine_type_id = $(this).val();
            wine_form.toggle_blend_wine_types_container(wine_type_id);
            wine_form.set_default_pairings(wine_type_id);
        });

        // Fill-out SEO title and image name when a name is entered
        $("#id_name").blur(function(){
            var $seo_title = $("#id_seo_title");
            var $seo_image_name = $("#id_seo_image_name");
            if($seo_title.val() == ""){
                $seo_title.val($(this).val());
            }
            if($seo_image_name.val() == ""){
                $seo_image_name.val($.slugify($(this).val()));
            }
        });

        // Fill-out SEO description when short description is entered
        $("#id_short_description").blur(function(){
            var $seo_description = $("#id_seo_description");
            if($seo_description.val() == ""){
                $seo_description.val($(this).val());
            }
        });

        // Calculates GST and WET from buying price
        $("#id_buying_price").keyup(function(){
            var gst_percentage = 10;
            var wet_percentage = 29;
            var selling_price = parseFloat($(this).val());
            var gst_paid = selling_price - (selling_price / (1+gst_percentage/100));
            var selling_price_without_gst = selling_price - gst_paid;
            var wet_paid = selling_price_without_gst - (selling_price_without_gst / (1+wet_percentage/100));
            $("#id_buying_gst_price").val(number_format(gst_paid, 2, '.', ','));
            $("#id_buying_wet_price").val(number_format(wet_paid, 2, '.', ','));
        });

        // Makes GST and WET fields readonly
        $("#id_buying_gst_price").addClass('readonly').attr('readonly', true);
        $("#id_buying_wet_price").addClass('readonly').attr('readonly', true);

    },

    // Jquery Events
    setup_upload: function() {

        // Dropzone options
        Dropzone.options.dropzone = {
            paramName: "file", // The name that will be used to transfer the file
            maxFilesize: 4, // MB
            addRemoveLinks: true,
            acceptedFiles: ".jpg,.png",
            uploadMultiple: false,
            parallelUploads: 1,
            dictDefaultMessage: "Drop Files Here or Click to Add Photos",
            init: function() {
                var $dropzone = this;

                // Preloads images already on the server
                $.each($attr.wine_photos, function(key, file) {
                    var mockFile = {
                        name: file.name,
                        size: file.size,
                        is_primary: file.is_primary ? true : false,
                        product_photo_id: file.product_photo_id,
                    };
                    $dropzone.emit("addedfile", mockFile);
                    wine_form.create_cover_checkbox(mockFile, {
                        is_primary: mockFile.is_primary,
                        product_photo_id: mockFile.product_photo_id
                    });
                    $dropzone.createThumbnailFromUrl(mockFile, file.url);
                    $dropzone.emit("complete", mockFile);
                });

                // After an upload, add checkbox to let the user pick the cover photo
                $dropzone.on("success", function(file, response) {
                    wine_form.create_cover_checkbox(file, response);
                });

                // After removing a file we need to also delete from the db and file system
                $dropzone.on("removedfile", function(file) {
                    var remove_id = file.product_photo_id;
                    $.post($attr.upload_url, {remove_id: remove_id}, function(data, status){
                        //alert("Remove - Data: " + data + "\nStatus: " + status);
                    });
                });

                // On uploading a file, we mark the flag as true to stop form submission
                $dropzone.on("sending", function() {
                    $attr.uploading = true;
                });

                // On complete, we mark the flag as true to allow form submission again
                $dropzone.on("complete", function() {
                    if($dropzone.getQueuedFiles().length == 0 && $dropzone.getUploadingFiles().length == 0){
                        $attr.uploading = false;
                    }
                });

            }
        };

    }

};
