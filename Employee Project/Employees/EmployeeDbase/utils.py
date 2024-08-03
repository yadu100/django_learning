from .models import EmployeeDatabase
from django.db.models import Q



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def SerachItem(request):
    #extracting search query from get
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    #print(search_query)

    ###filtering based on name or designation or employeeid###

    EmployeeDatabaseItem = EmployeeDatabase.objects.distinct().filter(Q(name__icontains=search_query) | Q(employee_id__startswith=search_query) 
                                                           |Q(designation__startswith=search_query))
    
    return EmployeeDatabaseItem, search_query



def Paginate(request, EmployeeDatabaseItem):

     ##### - - - - - - Pagination starts ------------ #####
    page = request.GET.get('page')
    no_of_items = 2
    paginator = Paginator(EmployeeDatabaseItem, no_of_items)


    try:
        EmployeeDatabaseItem = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        EmployeeDatabaseItem = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        EmployeeDatabaseItem = paginator.page(page)


### - - - - - optional - - - - - - - - ###

    left_index = int(page)-4
    if left_index<1:
        left_index=1

    right_index = int(page)+4
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages+1
    
    custom_range = range(left_index,right_index)


    return EmployeeDatabaseItem, custom_range, paginator