import imp
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    context  = {"message" : ""}
    return render(request, 'automation/index.html', context)

def upData(request, datatype):
    try:
        if datatype == 'calculations':
            from .models import CuboidData
            values = CuboidData.objects.filter().order_by('-id').values('edge_a', 'edge_b', 'edge_c', 'surface_area', 'volume', 'perimeter', 'addedDate')
            finalResult = "Results - <br><br>"
            if len(values) > 30:
                values = values[:30]

            for each in values:
                finalResult += "Length : " + str(each["edge_a"]) + "&emsp;&emsp;Breadth : " + str(each["edge_b"]) + "&emsp;&emsp;Height : " + str(each["edge_c"]) + "&emsp;&emsp;Surface Area : " + \
                str(each["surface_area"]) + "&emsp;&emsp;Volume : " + str(each["volume"]) + "&emsp;&emsp;Perimeter : " + str(each["perimeter"]) + "&emsp;&emsp;Date : " + str(each["addedDate"]) + "<br><br>"

            return HttpResponse(finalResult)
        
        if datatype == 'calculate':
            from .models import CuboidData

            edge_a = request.POST.get('edge_a', None)
            edge_b = request.POST.get('edge_b', None)
            edge_c = request.POST.get('edge_c', None)

            from .functions import Cuboid
            new_cuboid = Cuboid()
            new_cuboid.perform_action_inputs(edge_a, edge_b, edge_c)
            print("Volume - " +str(new_cuboid.volume))
            print("Surface Area - " +  str(new_cuboid.surface_area))
            print("Perimeter - " + str(new_cuboid.perimeter))  

            if edge_a != None and edge_b != None and edge_c != None:
                newEntry = CuboidData(edge_a=edge_a, edge_b=edge_b, edge_c=edge_c, surface_area=new_cuboid.surface_area, volume=new_cuboid.volume, perimeter=new_cuboid.perimeter)
                newEntry.save()

            finalResult = "Results - <br><br>"
            finalResult += "Length : " + str(edge_a) + "&emsp;&emsp;Breadth : " + str(edge_b) + "&emsp;&emsp;Height : " + str(edge_c) + "&emsp;&emsp;Surface Area : " + \
            str(new_cuboid.surface_area) + "&emsp;&emsp;Volume : " + str(new_cuboid.volume) + "&emsp;&emsp;Perimeter : " + str(new_cuboid.perimeter) + "<br><br>"                        

            return HttpResponse(finalResult)

    except Exception as upDataException:
        print("Up Data Exception - " + str(upDataException))

# def calculate(request):
#     try:

#         new_cuboid = Cuboid()
#         new_cuboid.perform_action_inputs()
#         print("Volume - " +str(new_cuboid.volume))
#         print("Surface Area - " +  str(new_cuboid.surface_area))
#         print("Perimeter - " + str(new_cuboid.perimeter))        


#     except Exception as calculateException:
#         print("Exception - " + str(calculateException))