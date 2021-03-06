from dataEntry import runentry
from api.models import *
from activity.models import Transactions, CGUser, CGUserNew
import re

import datetime
def cleanstring(query):
    query = query.strip()
    query = re.sub('\s{2,}', ' ', query)
    query = re.sub(r'^"|"$', '', query)
    query = query.title()
    return query


# Taxes.objects.all().delete()
# runentry.loadTaxes('States_Taxes.csv')
#
# Bills.objects.all().delete()

# Bookings Job Flag Correctionn
# bookings = Bookings.objects.all()
# for booking in bookings:
#     if booking.status == "Job Completed" or booking.status == "Feedback Taken":
#         booking.job_completion_flag = True
#         booking.save()
# CRV Correction

# vehicles = Vehicle.objects.filter(make = "Honda", model = "CR-V",fuel_type = "Petrol")
# for vehicle in vehicles:
#     vehicle.model = "CRV"
#     vehicle.save()
#
# ServiceParts = ServicePart.objects.filter(make="Honda", model="CR-V",fuel_type = "Petrol")
# for sparts in ServiceParts:
#     sparts.model = "CRV"
#     sparts.save()
#
# Services = Services.objects.filter(make="Honda", model="CR-V", fuel_type="Petrol")
# for Service in Services:
#     Service.model = "CRV"
#     Service.save()


# bookings = Bookings.objects.filter(status="Cancelled",booking_flag = True)
# for booking in bookings:
#     if booking.status == "Cancelled":
#         print booking.booking_id
#         booking.booking_flag = False
#         booking.status = "Lead"
#         booking.follow_up_date = booking.date_booking + datetime.timedelta(days=90)
#         booking.follow_up_time = datetime.time(9, 30, 0, 0)
#         booking.save()

        # BookingsBackup.objects.all().delete()
# for booking in bookings:
#     tt = BookingsBackup(booking_flag=booking.booking_flag,
#                         booking_id=booking.booking_id,
#                         booking_timestamp=booking.booking_timestamp,
#                         cust_id=booking.cust_id,
#                         cust_name=booking.cust_name,
#                         cust_make=booking.cust_make,
#                         cust_model=booking.cust_model,
#                         cust_vehicle_type=booking.cust_vehicle_type,
#                         cust_fuel_varient=booking.cust_fuel_varient,
#                         cust_regnumber=booking.cust_regnumber,
#                         cust_number=booking.cust_number,
#                         cust_email=booking.cust_email,
#                         cust_address=booking.cust_address,
#                         cust_locality=booking.cust_locality,
#                         cust_city=booking.cust_city,
#                         service_items=booking.service_items,
#                         price_total=booking.price_total,
#                         price_labour=booking.price_labour,
#                         price_part=booking.price_part,
#                         price_discount=booking.price_discount,
#                         date_booking=booking.date_booking,
#                         time_booking=booking.time_booking,
#                         date_delivery=booking.date_delivery,
#                         is_paid=booking.is_paid,
#                         amount_paid=booking.amount_paid,
#                         coupon=booking.coupon,
#                         status=booking.status,
#                         comments=booking.comments,
#                         jobssummary=booking.jobssummary,
#                         source=booking.source,
#                         agent=booking.agent,
#                         estimate_history=booking.estimate_history,
#                         customer_notes=booking.customer_notes,
#                         booking_user_type=booking.booking_user_type,
#                         booking_user_name=booking.booking_user_name,
#                         booking_user_number=booking.booking_user_number,
#                         clickgarage_flag=booking.clickgarage_flag,
#                         booking_owner=booking.booking_owner,
#                         odometer=booking.odometer,
#                         escalation_flag=booking.escalation_flag,
#                         bill_id=booking.bill_id,
#                         bill_generation_flag=booking.bill_generation_flag,
#                         payment_status=booking.payment_status,
#                         feedback_1=booking.feedback_1,
#                         feedback_2=booking.feedback_2,
#                         follow_up_date=booking.follow_up_date,
#                         follow_up_time=booking.follow_up_time,
#                         follow_up_status=booking.follow_up_status)
#     tt.save()

#     booking.bill_generation_flag = False
#     booking.bill_id = ""
    # item_list =[]
    # total_price = 0
    # total_part = 0
    # total_labour = 0
    # total_discount = 0
    # for item in booking.service_items:
    #     try:
    #         if item['type'] == "Part":
    #             total_price = total_price + float(item['price'])
    #             total_part = total_part + float(item['price'])
    #         elif item['type'] == "Consumable":
    #             total_price = total_price + float(item['price'])
    #             total_part = total_part + float(item['price'])
    #         elif item['type'] == "Lube":
    #             total_price = total_price + float(item['price'])
    #             total_part = total_part + float(item['price'])
    #
    #         elif item['type'] == "Labour":
    #             total_price = total_price + float(item['price'])
    #             total_labour = total_labour + float(item['price'])
    #
    #         elif item['type'] == "Discount":
    #             total_price = total_price - float(item['price'])
    #             total_discount = total_discount + float(item['price'])
    #     except:
    #         total_price = total_price + float(item['price'])
    #         total_labour = total_labour + float(item['price'])
    #
    # booking.price_total = total_price
    # booking.price_part = total_part
    # booking.price_labour = total_labour
    # booking.price_discount = total_discount
    # booking.frozen_flag = False
    # booking.settlement_flag = False
    # booking.purchase_price_total = total_price
    # booking.save()



# bookings = Bookings.objects.all()
# for booking in bookings:
#     jobs_summary = booking.comments
#     total_items = jobs_summary.split(", ")
#     items = []
#     for item in total_items:
#         if (item != "" and item != " "):
#             obj = {'Job':item,
#                 'Price':"0"}
#             items.append(obj)
#     booking.jobssummary = items
#     booking.save()

# users = CGUserNew.objects.all()
#
# for user in users:
#     print user.contact_no
#     if user.user_address == "" or user.user_address == None:
#         try:
#             user.user_address = user.user_saved_address[0]['address']
#         except:
#             None
#         try:
#             user.user_locality = user.user_saved_address[0]['locality']
#         except:
#             None
#         try:
#             user.user_city = user.user_saved_address[0]['city']
#         except:
#             None
#         user.save()
# Users = CGUser




# To Uncomment

Partsdatabase.objects.all().delete()

bookings = Bookings.objects.filter(booking_flag = False)
partsdata = ServicePart.objects.all()
labourdata = ServiceLabour.objects.all()



i =0
for part in bookings:
    make = part.cust_make
    model = part.cust_model
    fuel_type = part.cust_fuel_varient
    partslist = part.service_items
    for prt in partslist:
        i = i + 1
        name = prt['name']
        quantity = prt['quantity']
        unit_price = prt['unit_price']
        price = prt['price']
        type = prt['type']
        # print name
        name = cleanstring(name)
        name = name.title()
        print ("Booking " + str(i) + ' ' + make + ' ' + model + ' ' + fuel_type + ' ' + name)
        findPart = Partsdatabase.objects.filter(make=make, model=model, fuel_type=fuel_type,
                                                name=name)
        if len(findPart):
            findPart = findPart[0]
            findPart.clickgarage_flag = True
            findPart.agent_id = "ClickGarage"
            findPart.make = make
            findPart.model = model
            findPart.fuel_type = fuel_type
            findPart.name = name
            findPart.type = type
            findPart.quantity = quantity
            findPart.unit_price = unit_price
            findPart.price = price
            findPart.save()
        else:
            pa = Partsdatabase(
                clickgarage_flag=True
                , agent_id="ClickGarage"
                , make=make
                , model=model
                , fuel_type=fuel_type
                , name=name
                , type=type
                , quantity=quantity
                , unit_price=unit_price
                , price=price)
            pa.save()




for part in partsdata:
    make 				= part.make
    model 				= part.model
    fuel_type 			= part.fuel_type
    partslist           = part.default_components
    for prt in partslist:
        i = i + 1

        name = prt['name']
        quantity = prt['quantity']
        unit_price = prt['unit_price']
        price = prt['price']
        type = prt['type']
        print ("Part " + str(i) + ' ' + make + ' ' + model + ' ' + fuel_type + ' ' + name)
        name = cleanstring(name)

        # print name
        findPart =  Partsdatabase.objects.filter(make=make,model=model,fuel_type = fuel_type,name = name)
        if len(findPart):
            findPart = findPart[0]
            findPart.clickgarage_flag = True
            findPart.agent_id = "ClickGarage"
            findPart.make = make
            findPart.model = model
            findPart.fuel_type = fuel_type
            findPart.name = name
            findPart.type = type
            findPart.quantity = quantity
            findPart.unit_price = unit_price
            findPart.price = price
            findPart.save()
        else:
            pa = Partsdatabase(
                clickgarage_flag=True
                , agent_id="ClickGarage"
                , make=make
                , model=model
                , fuel_type=fuel_type
                , name=name
                , type=type
                , quantity=quantity
                , unit_price=unit_price
                , price=price)
            pa.save()

AllVehicle = Vehicle.objects.filter(car_bike = "Car")
for vehicle in AllVehicle:
    make = vehicle.make
    model = vehicle.model
    fuel_type = vehicle.fuel_type
    type = vehicle.type
    car_bike = vehicle.car_bike
    AllService = ServiceLabour.objects.filter(type=type, car_bike=car_bike)
    for prt in AllService:
        i = i + 1
        if prt.job_sub_cat == "NA":
            name = prt.job_name
        else:
            name = prt.job_name + ' ' + prt.job_sub_cat

        name = cleanstring(name)
        quantity = "1"
        unit_price = prt.total_price
        price = (float(prt.total_price) - float(prt.discount)) *1.18
        type = "Labour"
        print ("Labour " + str(i) + ' ' + make + ' ' + model + ' ' + fuel_type + ' ' + name)

        findPart = Partsdatabase.objects.filter(make=make, model=model, fuel_type=fuel_type, name=name)
        if len(findPart):
            findPart = findPart[0]
            findPart.clickgarage_flag = True
            findPart.agent_id = "ClickGarage"
            findPart.make = make
            findPart.model = model
            findPart.fuel_type = fuel_type
            findPart.name = name
            findPart.type = type
            findPart.quantity = quantity
            findPart.unit_price = unit_price
            findPart.price = price
            findPart.save()
        else:
            pa = Partsdatabase(
                clickgarage_flag=True
                , agent_id="ClickGarage"
                , make=make
                , model=model
                , fuel_type=fuel_type
                , name=name
                , type=type
                , quantity=quantity
                , unit_price=unit_price
                , price=price)
            pa.save()

