# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from wannamigrate.director.manage import process_data_for_situation
import itertools
import collections




#########################
# Migration functions
#########################
def populate_situations( apps, schema_editor ):
    """
        Creates the basic structure for the initial situations, missions and objectives.
        :param: apps A reference to the apps.
        :param: schema_editor A reference to the schema_editor.
    """

    ###################
    # Useful constants
    ###################
    AUSTRALIA_ID = 117
    CANADA_ID = 204
    LIVE_AND_WORK_ID = 1
    STUDY_ID = 2





    ############################
    # LIVE AND WORK IN CANADA
    ############################

    live_and_work_in_canada = \
    [
        {
            "title": "Canada",
            "objectives":
            [
                {
                    "title": "Why immigrate to Canada?",
                    "optional": False,
                    "description": "Learn about the country, immigration history and future prospects",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjheEtlVm0wMUk1cEE/preview",
                        },
                },

                {
                    "title": "Planning your move",
                    "optional": False,
                    "description" : "Learn the first steps you need to make in order to start your immigration process",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhOVJmbVpHalpOalU/preview",
                        },
                },
            ]
        },

        {
            "title": "Visa Type",
            "objectives":
            [
                {
                    "title": "Immigration Points System",
                    "optional": False,
                    "description": "Check if you qualify for a permanent visa using the points-based immigration system",
                    "content":
                        {
                            "type": "redirect_content",
                            "url": "https://wannamigrate.com/immigration-calculator",
                            "progress_uri" : "wannamigrate.points.views.get_progress",
                            "blank": True,
                        }
                },

                {
                    "title": "Skype Evaluation",
                    "optional": True,
                    "description": "Talk to an expert to have your situation evaluated",
                    "content":
                        {
                            "type": "redirect_content",
                            "url": "https://www.wannamigrate.com/26/humberto-moreira",
                            "progress_uri": None,
                            "blank": True,
                        }
                },

                {
                    "title": "Your visa type",
                    "optional": False,
                    "description": "Discover the immigration options and wich visa is more appropriate for your case",
                    "content":
                        {
                            "type": "generic_container",
                            "layout": "linear",
                            "content":
                            [
                                {
                                    "type": "iframe_content",
                                    "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhZjZRM3g4NUpielE/preview"
                                },
                                {
                                    "type": "form_content",
                                    "question": "Do you already know your visa type?",
                                    "choices":
                                    [
                                        ( "NO, I'm still learning about it", 0 ),
                                        ( "Yes, Student Visa", 100 ),
                                        ( "Yes, Express Entry", 100 ),
                                        ( "Yes, Self-Employed", 100 ),
                                        ( "Yes, Live-in Caregivers", 100 ),
                                        ( "Yes, Start-up Visa", 100 ),
                                        ( "Yes, Family Sponsorship", 100 ),
                                        ( "Yes, Company Sponsorship", 100 ),
                                        ( "Yes, Province Programs", 100 ),
                                        ( "Yes, Other", 100 ),
                                    ]
                                },
                            ]
                        }
                },
            ]
        },

        {
            "title": "Language Requirements",
            "objectives":
            [
                {
                    "title": "Requirements and hints to learn English",
                    "optional": False,
                    "description": "Understand the level required and use our study plan",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhY2x4dXNSLU1tSnc/preview"
                        }
                },

                {
                    "title": "English Evaluation",
                    "optional": False,
                    "description": "Test your English skills",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },

                {
                    "title": "IELTS Preparation",
                    "optional": False,
                    "description": "Get ready for your certification exam",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Education Requirements",
            "objectives":
            [
                {
                    "title": "Requirements and Assessment",
                    "optional": False,
                    "description": "Understand what education level you need and how to do a \"Education Credential Assessment\"",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhbEtPUEg5R1VjRzA/preview",
                        },
                },
            ]
        },

        {
            "title": "Jobs",
            "objectives":
            [
                {
                    "title": "Looking for jobs over the internet",
                    "optional": False,
                    "description": "Learn techniques to apply for available positions in Canada",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhakxudldYbGI4dk0/preview",
                        },
                },

                {
                    "title": "Build Your Resumé",
                    "optional": False,
                    "description": "Learn how to create your Canadian Resumé",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhYWI1MkVHbHVsMm8/preview",
                        },
                },

                {
                    "title": "Build your Cover-Letter",
                    "optional": False,
                    "description": "Learn how to create your Canadian Cover-Letter",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhNUFYZFI2UjQtejQ/preview"
                        },
                },

                {
                    "title": "Build Your Linkedin and Online Presence",
                    "optional": False,
                    "description": "Learn how to create your Linkedin profile and online presence",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhblZrMm5iaWNBUUU/preview"
                        },
                },
            ]
        },

        {
            "title": "Visa Application",
            "objectives":
            [
                {
                    "title": "Your immigration plan",
                    "optional": False,
                    "description": "How to plan and execute your visa application",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhTE1MZ2EtS2NURHc/preview"
                        },
                },

                {
                    "title": "Proof of funds",
                    "optional": False,
                    "description": "How much you need and how to provide proof",
                    "content":
                        {
                            "type": "generic_container",
                            "layout": "linear",
                            "content":
                                [
                                    {
                                        "type": "iframe_content",
                                        "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhb1lGX0lLNnZWaEE/preview",
                                    },
                                    {
                                        "type": "form_content",
                                        "question": "Do you already have the required proof of funds?",
                                        "choices":
                                            [
                                                ( "Yes", 100 ),
                                                ( "No", 0 ),
                                            ]
                                    },
                                ],
                        },
                },

                {
                    "title": "Language and Education Certificates",
                    "optional": False,
                    "description": "Certificates",
                    "content":
                        {
                            "type": "form_content",
                            "question": "Do you already have the language results and the Education Credential Assessment certificate?",
                            "choices":
                                [
                                    ( "Yes", 100 ),
                                    ( "No", 0 ),
                                ]
                        },
                },

                {
                    "title": "Proof of Past Employment",
                    "optional": False,
                    "description": "Templates for proof of past employment",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhN0RZeVpoU3A0TEk/preview",
                        },
                },

                {
                    "title": "Sending your application",
                    "optional": False,
                    "description": "Learn where and how to submit your visa application",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Moving to Canada",
            "objectives":
            [
                {
                    "title": "Be prepared to move",
                    "optional": False,
                    "description": "What to do before and after you move to Canada",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhLWVkczB3a1dZbGs/preview",
                        },
                },

                {
                    "title": "Visa Approval",
                    "optional": False,
                    "description": "Set your visa status",
                    "content":
                        {
                            "type": "form_content",
                            "question": "What is your visa application status?",
                            "choices":
                                [
                                    ( "Not sent", 0 ),
                                    ( "Sent", 50 ),
                                    ( "Approved", 100 ),
                                ]
                        },
                },
            ]
        },
    ]

    # Processes the data for LIVE AND WORK IN CANADA
    process_data_for_situation( live_and_work_in_canada, CANADA_ID, LIVE_AND_WORK_ID )





    ######################
    # STUDY IN CANADA
    ######################
    study_in_canada = \
    [
        {
            "title": "Canada",
            "objectives":
            [
                {
                    "title": "Why Study in Canada?",
                    "optional": False,
                    "description": "Learn about the country, immigration history and future prospects",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhLWU0THRlV1ZORTg/preview",
                        },
                },

                {
                    "title": "Studying in Canada",
                    "optional": False,
                    "description" : "Learn the first steps you need to make in order to start you immigration process",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhSEhmYmZpMFRYTFk/preview",
                        },
                },
            ]
        },

        {
            "title": "Course of choice",
            "objectives":
            [
                {
                    "title": "Find a Course",
                    "optional": False,
                    "description": "Learn how to search for the course in the area of your choice",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhemFySFVIbGRaZjg/preview",
                        }
                },
            ]
        },

        {
            "title": "Language Requirements",
            "objectives":
            [
                {
                    "title": "Requirements and hints to learn English",
                    "optional": False,
                    "description": "Understand the level required and use our study plan",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhRXNua2hMLTEzaVk/preview"
                        }
                },

                {
                    "title": "English Evaluation",
                    "optional": False,
                    "description": "Test your English skills",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },

                {
                    "title": "IELTS Preparation",
                    "optional": False,
                    "description": "Get ready for your certification exam",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Education Requirements",
            "objectives":
            [
                {
                    "title": "Requirements and Assessment",
                    "optional": False,
                    "description": "Understand what education level you need and how to do a \"Education Credential Assessment\"",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhRnF5THBWUUVXeUU/preview",
                        },
                },
            ]
        },

        {
            "title": "Jobs",
            "objectives":
            [
                {
                    "title": "Looking for jobs over the internet",
                    "optional": False,
                    "description": "Learn techniques to apply for available positions in Canada",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhbnU5WDlXLWRaYU0/preview",
                        },
                },

                {
                    "title": "Build Your Resumé",
                    "optional": False,
                    "description": "Learn how to create your Canadian Resumé",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhREM4NkNSNkNLRGs/preview",
                        },
                },

                {
                    "title": "Build your Cover-Letter",
                    "optional": False,
                    "description": "Learn how to create your Canadian Cover-Letter",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhQThoNlFRUlZ2LUk/preview"
                        },
                },

                {
                    "title": "Build Your Linkedin and Online Presence",
                    "optional": False,
                    "description": "Learn how to create your Linkedin profile and online presence",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhbnQxTlZoQndjbkE/preview"
                        },
                },
            ]
        },

        {
            "title": "Visa Application",
            "objectives":
            [
                {
                    "title": "Your immigration plan",
                    "optional": False,
                    "description": "How to plan and execute your visa application",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhOEVJQ044cXE1VjQ/preview"
                        },
                },

                {
                    "title": "Proof of funds",
                    "optional": False,
                    "description": "How much you need and how to provide proof",
                    "content":
                        {
                            "type": "generic_container",
                            "layout": "linear",
                            "content":
                                [
                                    {
                                        "type": "iframe_content",
                                        "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhS05NQ0dQS2hVMnc/preview",
                                    },
                                    {
                                        "type": "form_content",
                                        "question": "Do you already have the required proof of funds?",
                                        "choices":
                                            [
                                                ( "Yes", 100 ),
                                                ( "No", 0 ),
                                            ]
                                    },
                                ],
                        },
                },

                {
                    "title": "Language and Education Certificates",
                    "optional": False,
                    "description": "Certificates",
                    "content":
                        {
                            "type": "form_content",
                            "question": "Do you already have the language results and the Education Credential Assessment certificate?",
                            "choices":
                                [
                                    ( "Yes", 100 ),
                                    ( "No", 0 ),
                                ]
                        },
                },

                {
                    "title": "Sending your application",
                    "optional": False,
                    "description": "Learn where and how to submit your visa application",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Moving to Canada",
            "objectives":
            [
                {
                    "title": "Be prepared to move",
                    "optional": False,
                    "description": "What to do before and after you move to Canada",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhalctczVrdkNfejA/preview",
                        },
                },

                {
                    "title": "Visa Approval",
                    "optional": False,
                    "description": "Set your visa status",
                    "content":
                        {
                            "type": "form_content",
                            "question": "What is your visa application status?",
                            "choices":
                                [
                                    ( "Not sent", 0 ),
                                    ( "Sent", 50 ),
                                    ( "Approved", 100 ),
                                ]
                        },
                },
            ]
        },
    ]

    # Processes the data for STUDY IN CANADA
    process_data_for_situation( study_in_canada, CANADA_ID, STUDY_ID )




    ############################
    # LIVE AND WORK IN AUSTRALIA
    ############################

    live_and_work_in_australia = \
    [
        {
            "title": "Australia",
            "objectives":
            [
                {
                    "title": "Why immigrate to Australia?",
                    "optional": False,
                    "description": "Learn about the country, immigration history and future prospects",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhakFDenpBdjI1OFE/preview",
                        },
                },

                {
                    "title": "Planning your move",
                    "optional": False,
                    "description" : "Learn the first steps you need to make in order to start your immigration process",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhcU9HVVRtUmVsZ1E/preview",
                        },
                },
            ]
        },

        {
            "title": "Visa Type",
            "objectives":
            [
                {
                    "title": "Immigration Points System",
                    "optional": False,
                    "description": "Check if you qualify for a permanent visa using the points-based immigration system",
                    "content":
                        {
                            "type": "redirect_content",
                            "url": "https://wannamigrate.com/immigration-calculator",
                            "progress_uri" : "wannamigrate.points.views.get_progress",
                            "blank": True,
                        }
                },

                {
                    "title": "Skype Evaluation",
                    "optional": True,
                    "description": "Talk to an expert to have your situation evaluated",
                    "content":
                        {
                            "type": "redirect_content",
                            "url": "https://www.wannamigrate.com/26/humberto-moreira",
                            "progress_uri": None,
                            "blank": True,
                        }
                },

                {
                    "title": "Your visa type",
                    "optional": False,
                    "description": "Discover the immigration options and wich visa is more appropriate for your case",
                    "content":
                        {
                            "type": "generic_container",
                            "layout": "linear",
                            "content":
                            [
                                {
                                    "type": "iframe_content",
                                    "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhOWppbkVlQ0FQeDA/preview"
                                },
                                {
                                    "type": "form_content",
                                    "question": "Do you already know your visa type?",
                                    "choices":
                                    [
                                        ( "NO, I'm still learning about it", 0 ),
                                        ( "Yes, Student Visa", 100 ),
                                        ( "Yes, Express Entry", 100 ),
                                        ( "Yes, Self-Employed", 100 ),
                                        ( "Yes, Live-in Caregivers", 100 ),
                                        ( "Yes, Start-up Visa", 100 ),
                                        ( "Yes, Family Sponsorship", 100 ),
                                        ( "Yes, Company Sponsorship", 100 ),
                                        ( "Yes, Province Programs", 100 ),
                                        ( "Yes, Other", 100 ),
                                    ]
                                },
                            ]
                        }
                },
            ]
        },

        {
            "title": "Language Requirements",
            "objectives":
            [
                {
                    "title": "Requirements and hints to learn English",
                    "optional": False,
                    "description": "Understand the level required and use our study plan",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhU05fRExaazRsdzA/preview"
                        }
                },

                {
                    "title": "English Evaluation",
                    "optional": False,
                    "description": "Test your English skills",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },

                {
                    "title": "IELTS Preparation",
                    "optional": False,
                    "description": "Get ready for your certification exam",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Skills Requirements",
            "objectives":
            [
                {
                    "title": "Requirements and Assessment",
                    "optional": False,
                    "description": "Understand what education level you need and how to do a \"Skills Assessment\"",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhZlhLWmVtS2Jlbjg/preview",
                        },
                },
            ]
        },

        {
            "title": "Jobs",
            "objectives":
            [
                {
                    "title": "Looking for jobs over the internet",
                    "optional": False,
                    "description": "Learn techniques to apply for available positions in Australia",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhdkdoeS1abDZ2bWM/preview",
                        },
                },

                {
                    "title": "Build Your Resumé",
                    "optional": False,
                    "description": "Learn how to create your Australian Resumé",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhY19VT1hxRi0zNFk/preview",
                        },
                },

                {
                    "title": "Build your Cover-Letter",
                    "optional": False,
                    "description": "Learn how to create your Australian Cover-Letter",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhRW40ZnB1NXlsMmc/preview"
                        },
                },

                {
                    "title": "Build Your Linkedin and Online Presence",
                    "optional": False,
                    "description": "Learn how to create your Linkedin profile and online presence",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhSS1lNGdudWpISGs/preview"
                        },
                },
            ]
        },

        {
            "title": "Visa Application",
            "objectives":
            [
                {
                    "title": "Your immigration plan",
                    "optional": False,
                    "description": "How to plan and execute your visa application",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhMmRQVkFYaWdIdHM/preview"
                        },
                },

                {
                    "title": "Proof of funds",
                    "optional": False,
                    "description": "How much you need and how to provide proof",
                    "content":
                        {
                            "type": "generic_container",
                            "layout": "linear",
                            "content":
                                [
                                    {
                                        "type": "iframe_content",
                                        "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhbWVwb1VDXy1pb2s/preview",
                                    },
                                    {
                                        "type": "form_content",
                                        "question": "Do you already have the required proof of funds?",
                                        "choices":
                                            [
                                                ( "Yes", 100 ),
                                                ( "No", 0 ),
                                            ]
                                    },
                                ],
                        },
                },

                {
                    "title": "Language and Education Certificates",
                    "optional": False,
                    "description": "Certificates",
                    "content":
                        {
                            "type": "form_content",
                            "question": "Do you already have the language results and the Education Credential Assessment certificate?",
                            "choices":
                                [
                                    ( "Yes", 100 ),
                                    ( "No", 0 ),
                                ]
                        },
                },

                {
                    "title": "Proof of Past Employment",
                    "optional": False,
                    "description": "Templates for proof of past employment",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhNzNPRW1PQkNRSVE/preview",
                        },
                },

                {
                    "title": "Sending your application",
                    "optional": False,
                    "description": "Learn where and how to submit your visa application",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Moving to Australia",
            "objectives":
            [
                {
                    "title": "Be prepared to move",
                    "optional": False,
                    "description": "What to do before and after you move to Australia",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhQW15eVQ3T3dTMlk/view?usp=sharing",
                        },
                },

                {
                    "title": "Visa Approval",
                    "optional": False,
                    "description": "Set your visa status",
                    "content":
                        {
                            "type": "form_content",
                            "question": "What is your visa application status?",
                            "choices":
                                [
                                    ( "Not sent", 0 ),
                                    ( "Sent", 50 ),
                                    ( "Approved", 100 ),
                                ]
                        },
                },
            ]
        },
    ]

    # Processes the data for LIVE AND WORK IN AUSTRALIA
    process_data_for_situation( live_and_work_in_australia, AUSTRALIA_ID, LIVE_AND_WORK_ID )




    ############################
    # STUDY IN AUSTRALIA
    ############################
    study_in_australia = \
    [
        {
            "title": "Australia",
            "objectives":
            [
                {
                    "title": "Why study in Australia?",
                    "optional": False,
                    "description": "Learn about the country, immigration history and future prospects",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhLTBQbGpaWDEyTkE/preview",
                        },
                },

                {
                    "title": "Studying in Australia",
                    "optional": False,
                    "description" : "Learn the first steps you need to make in order to start your immigration process",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhWnhzRUhpMWVrdkU/preview",
                        },
                },
            ]
        },

        {
            "title": "Course of choice",
            "objectives":
            [

                {
                    "title": "Find a course",
                    "optional": False,
                    "description": "Learn how to search for the course in the area of your choice",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhWFFWMzQ4X09tbTA/preview",
                        }
                },
            ]
        },

        {
            "title": "Language Requirements",
            "objectives":
            [

                {
                    "title": "Requirements and hints to learn English",
                    "optional": False,
                    "description": "Understand the level required and use our study plan",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhdlZqbkZyMFAtUzA/preview"
                        }
                },

                {
                    "title": "English Evaluation",
                    "optional": False,
                    "description": "Test your English skills",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },

                {
                    "title": "IELTS Preparation",
                    "optional": False,
                    "description": "Get ready for your certification exam",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Education Requirements",
            "objectives":
            [
                {
                    "title": "Requirements and Assessment",
                    "optional": False,
                    "description": "Understand what education level you need and how to do a \"Skills Assessment\"",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhYi0wT1BJLWZpS2M/preview",
                        },
                },
            ]
        },

        {
            "title": "Jobs",
            "objectives":
            [
                {
                    "title": "Looking for jobs over the internet",
                    "optional": False,
                    "description": "Learn techniques to apply for available positions in Australia",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhOFlzV1hxUWZ5d1E/preview",
                        },
                },

                {
                    "title": "Build Your Resumé",
                    "optional": False,
                    "description": "Learn how to create your Australian Resumé",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhZEh2Y213cXJYcGc/preview",
                        },
                },

                {
                    "title": "Build your Cover-Letter",
                    "optional": False,
                    "description": "Learn how to create your Australian Cover-Letter",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhb1VMc0g4VllJQzQ/preview"
                        },
                },

                {
                    "title": "Build Your Linkedin and Online Presence",
                    "optional": False,
                    "description": "Learn how to create your Linkedin profile and online presence",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhOWdjQXQtV0wtNTA/preview"
                        },
                },
            ]
        },

        {
            "title": "Visa Application",
            "objectives":
            [
                {
                    "title": "Your immigration plan",
                    "optional": False,
                    "description": "How to plan and execute your visa application",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhck1semNYZnpEak0/preview"
                        },
                },

                {
                    "title": "Proof of funds",
                    "optional": False,
                    "description": "How much you need and how to provide proof",
                    "content":
                        {
                            "type": "generic_container",
                            "layout": "linear",
                            "content":
                                [
                                    {
                                        "type": "iframe_content",
                                        "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhQndfaHlSb0NBcFU/preview",
                                    },
                                    {
                                        "type": "form_content",
                                        "question": "Do you already have the required proof of funds?",
                                        "choices":
                                            [
                                                ( "Yes", 100 ),
                                                ( "No", 0 ),
                                            ]
                                    },
                                ],
                        },
                },

                {
                    "title": "Language and Skills Certificates",
                    "optional": False,
                    "description": "Certificates",
                    "content":
                        {
                            "type": "form_content",
                            "question": "Do you already have the language results and the Skills Assessment certificate?",
                            "choices":
                                [
                                    ( "Yes", 100 ),
                                    ( "No", 0 ),
                                ]
                        },
                },

                {
                    "title": "Sending your application",
                    "optional": False,
                    "description": "Learn where and how to submit your visa application",
                    "content":
                        {
                            "type": "html_content",
                            "html": "Available Soon"
                        }
                },
            ]
        },

        {
            "title": "Moving to Australia",
            "objectives":
            [
                {
                    "title": "Be prepared to move",
                    "optional": False,
                    "description": "What to do before and after you move to Australia",
                    "content":
                        {
                            "type": "iframe_content",
                            "url": "https://drive.google.com/file/d/0B3qN5CaSfrjhVEVENFZtUmEwT00/preview",
                        },
                },

                {
                    "title": "Visa Approval",
                    "optional": False,
                    "description": "Set your visa status",
                    "content":
                        {
                            "type": "form_content",
                            "question": "What is your visa application status?",
                            "choices":
                                [
                                    ( "Not sent", 0 ),
                                    ( "Sent", 50 ),
                                    ( "Approved", 100 ),
                                ]
                        },
                },
            ]
        },
    ]

    # Processes the data for LIVE AND WORK IN AUSTRALIA
    process_data_for_situation( study_in_australia, AUSTRALIA_ID, STUDY_ID )




#########################
# Migration configuration
#########################
class Migration(migrations.Migration):

    dependencies = [
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.RunPython( populate_situations )
    ]
