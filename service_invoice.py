services = {
   'Oil change': 35,
   'Tire rotation': 19,
   'Car wash': 7,
   'Car wax': 12
}


print("Davy's auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n")

service_1 = input('Select first service:\n')
service_2 = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")

if service_1 == '-' :
    service_1_cost = 0
    print('Service 1: No service')
else:
    service_1_cost = services[service_1]
    print('Service 1: {}, ${}'.format(service_1, service_1_cost))
    
    
    
if service_2 == '-' :
    service_2_cost = 0
    print('Service 2: No service')
else:
    service_2_cost = services[service_2]
    print('Service 2: {}, ${}'.format(service_2, service_2_cost))

total_service_cost = service_1_cost + service_2_cost

print('\nTotal: ${}'.format(total_service_cost))
