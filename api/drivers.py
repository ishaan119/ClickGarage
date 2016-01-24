from api.models import *
from django.http import HttpResponse

secret_string = "dmFydW5ndWxhdGlsaWtlc2dhbG91dGlrZWJhYg=="

def signUpDriver(request):
    if (request.method == 'POST') :
        b_unicode   = request.body.decode('utf-8')
        body        = json.loads(b_unicode)
        mobile      = body.get('mobile')
        name        = body.get('name')
        
        if (body.get('secret') && body.get('secret')=='anaconda') :
            driver, exists = Driver.objects.get_or_create(mobile=mobile, name=name)

            if exists :
                result = dict(status=True, message='User exists')

            else :
                driver.save()
                result = dict(status=True, mobile=mobile, rID=rID)

            return HttpResponse(result, content_type='application/json')

def fetchAllBookings(request):
    if (request.method == 'GET') :
        params = request.GET

        if (params.get('rID')) :
            all_bookings = list()
            #TODO show booking details
            return HttpResponse(all_bookings, content_type='application/json')

def updateBookingStatus(request):
    if (request.method == 'POST') :
        b_unicode   = request.body.decode('utf-8')
        body        = json.loads(b_unicode)

        if (request.POST.get('rID')) :
            mobile  = body.get('mobile')
            name    = body.get('name')
            status  = body.get('status')
            lat     = body.get('lat')
            lon     = body.get('lon')
            booking_id = body.get('booking_id')

            booking_object = DriverBookings(driver__name=name, 
                                            driver__mobile=mobile, 
                                            booking__booking_id=booking_id,
                                            status__status=status,
                                            lat=lat,
                                            lon=lon)
            booking_object.save()

            result = dict(status=True, message='updated')
            return HttpResponse(result, content_type='application/json')

def getDriverBookings(request):
    if (request.method == 'GET') :
        params = request.GET

        if (params.get('rID')) :
            mobile  = params.get('mobile')
            name    = params.get('name')

            bookings = DriverBookings.objects.filter(driver__name=name, driver__mobile=mobile)

            result = list()

            for booking in bookings : 
                booking_dict = dict()
                booking_details = booking.booking
                booking_dict['id'] = booking_details.booking_id 
                booking_dict['cust_id'] = booking_details.cust_id
                # TODO fill necessary details

                result.append(booking_dict)

            return HttpResponse(result, content_type='application/json')

