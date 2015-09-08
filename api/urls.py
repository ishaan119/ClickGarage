from django.conf.urls import include, url
#from django.conf.urls.defaults import patterns, include, url
#from django.conf import settings

#import api

#from access import features
urlpatterns = [
    url(r'fetch_all_cars/$','api.views.fetch_all_cars',name='fetch_all_cars'),
    url(r'fetch_car/$','api.views.fetch_car',name='fetch_car'),

    url(r'fetch_car_autocomplete/$','api.views.fetch_car_autocomplete',name='fetch_car_autocomplete'),

    #car_<servicename>, <servicename>_details
    # params : c_id,
    url(r'fetch_car_servicing/$','api.views.fetch_car_services',name='fetch_car_services'),
    # params : service_id
    url(r'fetch_servicing_details/$','api.views.fetch_car_servicedetails',name='fetch_car_servicedetails'),
    # params : none
    url(r'fetch_car_cleaning/$','api.views.fetch_car_cleaning',name='fetch_car_cleaning'),
    # params : service_id, c_id
    url(r'fetch_cleaning_details/$','api.views.fetch_clean_catservice',name='fetch_clean_catservice'),
    # params : none
    url(r'fetch_car_vas/$','api.views.fetch_car_vas',name='fetch_car_vas'),
    # params : service_id, c_id
    url(r'fetch_vas_details/$','api.views.fetch_vas_catservice',name='fetch_vas_catservice'),
    # params : c_id
    url(r'fetch_car_windshield/$','api.views.fetch_car_services',name='fetch_car_services'),
    # params : service_id
    url(r'fetch_windshield_details/$','api.views.fetch_car_servicedetails',name='fetch_car_servicedetails'),
    # url(r'fetch_car_servicedealercat/$','api.views.fetch_car_servicedealercat',name='fetch_car_servicedealercat'),
	
    url(r'fetch_all_cleaningdealer/$','api.views.fetch_all_cleaningdealer',name='fetch_all_cleaningdealer'),
    url(r'fetch_dealer_cleancat/$','api.views.fetch_dealer_cleancat',name='fetch_dealer_cleancat'),
    url(r'fetch_clean_catservice/$','api.views.fetch_clean_catservice',name='fetch_clean_catservice'),
    url(r'fetch_all_cleaningcat/$','api.views.fetch_all_cleaningcat',name='fetch_all_cleaningcat'),
    url(r'fetch_all_cleaningcatservices/$','api.views.fetch_all_cleaningcatservices',name='fetch_all_cleaningcatservices'),
      

    url(r'fetch_all_vasdealer/$','api.views.fetch_all_vasdealer',name='fetch_all_vasdealer'),
    url(r'fetch_dealer_vascat/$','api.views.fetch_dealer_vascat',name='fetch_dealer_vascat'),
    url(r'fetch_vas_catservice/$','api.views.fetch_vas_catservice',name='fetch_vas_catservice'),
    url(r'fetch_all_vascat/$','api.views.fetch_all_vascat',name='fetch_all_vascat'),
    url(r'fetch_all_vascatservices/$','api.views.fetch_all_vascatservices',name='fetch_all_vascatservices'),
      
    url(r'fetch_all_windshieldcatdetails/$','api.views.fetch_all_windshieldcatdetails',name='fetch_all_windshieldcatdetails'),
    url(r'fetch_all_windshieldservices/$','api.views.fetch_all_windshieldservices',name='fetch_all_windshieldservices'),
    url(r'fetch_car_windshieldcatdetails/$','api.views.fetch_car_windshieldcatdetails',name='fetch_car_windshieldcatdetails'),
    url(r'fetch_car_windshieldservices/$','api.views.fetch_car_windshieldservices',name='fetch_car_windshieldservices'),
            





    url(r'fetch_all_services/$','api.views.fetch_all_services',name='fetch_all_services'),
    # url(r'fetch_all_servicedealercat/$','api.views.fetch_all_servicedealercat',name='fetch_all_servicedealercat'),
    url(r'fetch_all_servicedealername/$','api.views.fetch_all_servicedealername',name='fetch_all_servicedealername'),
    
	url(r'fetch_car_tyres/$','api.views.fetch_car_tyres',name='fetch_car_tyres'),

    url(r'fetch_all_wheelservices/$','api.views.fetch_all_wheelservices',name='fetch_all_wheelservices'),
    url(r'fetch_all_wheelserviceprovider/$','api.views.fetch_all_wheelserviceprovider',name='fetch_all_wheelserviceprovider'),
    url(r'fetch_all_tyresales/$','api.views.fetch_all_tyresales',name='fetch_all_tyresales')
	
	
    ]
