from .models import User, Category, Subcategory, Applications
from .utils import str_to_binary, binary_to_str
from django.db.utils import IntegrityError, DataError
from .serializers import user_data_serializer, categories_serializer, sub_categories_serializer, application_serializer

def create_user(user_data, profile_picture):
    res = {}
    try:
        profile_picture = str_to_binary(profile_picture)
        user = User.objects.create(Name=user_data['name'],
                                    Email=user_data['email'],
                                    Password=user_data['password'],
                                    Profile_Picture=profile_picture,
                                    Admin=user_data['admin'])
        new_user = user_data_serializer(user)
        res = {'success': True, 'message': 'User Created Successfully', 'user_data': new_user}

    except IntegrityError:
        print("User Already Exist")
        res = {'success': False, 'message': 'User Already Exist'}

    except DataError:
        print("Incorrect Data. PLease Try Again!")
        res = {'success': False, 'message': 'Incorrect Data. PLease Try Again!'}

    except:
        print("Something went wrong. Please Try Again!")
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res


def user_login(email, password, admin):
    res = {}
    try:
        user = User.objects.filter(Email=email, Password=password, Admin=admin)
        user = user_data_serializer(user[0])
        res = {'success': True, 'message': 'User Logged In Succesfully!', 'user_data': user}
    except DataError:
        print("Incorrect Data. PLease Try Again!")
        res = {'success': False, 'message': 'Incorrect User Details. PLease Try Again!'}
    except:
        print("User Doesn't Exist")
        res = {'success': False, 'message': 'User Doesn\'t exist! Please Create an account!'}

    return res

def create_category(category_name, email):
    res = {}
    try:
        user = User.objects.filter(Email=email)
        if len(user) > 0 and user[0].Admin == True:
            new_category = Category.objects.create(Category_Name=category_name, Created_By_id=user[0].id)
            if new_category.id:
                res = {'success': True, 'message': 'Category Successfully Created!'}
            else:
                res = {'success': False, 'message': 'Category not created. Please Try Again'}
        else:
            res = {'success': False, 'message':'Category not created. Please Try Again'}
    except:
        res = {'success': False, 'message': 'Category not created. Please Try Again!'}
    return res

def create_sub_category(subcategory_name, category_name, email):
    res= {}
    try:
        user = User.objects.filter(Email=email)
        user = list(user)
        category = Category.objects.filter(Category_Name=category_name)
        if len(user) > 0 and user[0].Admin == True and len(category) > 0:
            new_subcategory = Subcategory.objects.create(SubCategory_Name=subcategory_name, Category_id=category[0].id, Created_By_id=user[0].id)
            if new_subcategory.id:
                res = {'success': True, 'message': 'Sub Category Successfully Created!'}
            else:
                res = {'success': False, 'message': 'Sub Category not created. Please Try Again'}
        else:
            res = {'success': False, 'message':'Sub Category not created. Please Try Again'}
    except:
        res = {'success': False, 'message': 'Sub Category not created. Please Try Again!'}
    return res

def get_categories():
    res = {}
    try:
        categories = Category.objects.all()
        categories = categories_serializer(categories)
        res = {'success': True, 'categories_data': categories}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def get_sub_categories(category_id):
    res = {}
    try:
        sub_categories = Subcategory.objects.filter(Category_id=category_id)
        sub_categories = sub_categories_serializer(sub_categories)
        res = {'success': True, 'subcategories_data': sub_categories}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def create_application(app_details, app_image):
    res = {}
    try:
        user = User.objects.filter(Email= app_details['email'])
        if len(user) == 1 and user[0].Admin == True:
            app_image = str_to_binary(app_image)
            application = Applications.objects.create(App_Name=app_details['app_name'], App_link=app_details['app_link'], Description=app_details['description'],
                                                        Points=app_details['points'], Application_Picture=app_image, Category_id=app_details['category_id'],
                                                        Subcategory_id=app_details['subcategory_id'], Created_By_id=user[0].id
                                                        )
            category = Category.objects.filter(id=application.Category_id)
            category = categories_serializer(category)[0]
            subcategory = Subcategory.objects.filter(id=application.Subcategory_id)
            subcategory = sub_categories_serializer(subcategory)[0]
            application = application_serializer([application])
            application = application[0]
            application['category'] = category
            application['subcategory'] = subcategory
            res = {'success': True, 'message': 'Application Create Succesfully.', 'app_details': application}
        elif len(user) == 1 and user[0].Admin == False:
            res = {'success': False, 'message': 'Only Admin can create Application'}
        else:
            res = {{'success': False, 'message': 'User Doesn\'t Exist. Please Create an account'}}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def get_application(app_name, app_id, email = None):
    res = {}
    try:
        application = Applications.objects.filter(id=app_id)
        downloaded_by_user = False
        if len(application) == 1:
            category = Category.objects.filter(id=application[0].Category_id)
            category = categories_serializer(category)[0]
            subcategory = Subcategory.objects.filter(id=application[0].Subcategory_id)
            subcategory = sub_categories_serializer(subcategory)[0]
            if email:
                user = User.objects.filter(Email=email)
                if len(user) == 1 and user[0].Admin == False:
                    if str(user[0].id) in application[0].Screenshots:
                        downloaded_by_user = True
            application = application_serializer(application)[0]
            application['category'] = category
            application['subcategory'] = subcategory
            application['downloaded_by_user'] = downloaded_by_user
            res = {'success': True, 'application_data': application}
        else:
            res = {'success': False, 'message': 'Application Doesn\'t Exists'}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def get_applications():
    res = {}
    try:
        applications = Applications.objects.all()
        applications = application_serializer(applications)
        res = {'success': True, 'applications_data': applications}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def download_application(email, app_id, screenshot):
    res = {}
    try:
        user = User.objects.filter(Email=email)
        if len(user) == 1 and user[0].Admin == False:
            application = Applications.objects.filter(id=app_id)
            screenshots = application[0].Screenshots
            if not screenshots.get(str(user[0].id), None):
                screenshots[str(user[0].id)] = {}
                screenshots[str(user[0].id)]['screenshot'] = screenshot
                updated_application = Applications.objects.filter(id=app_id).update(Screenshots= screenshots)
                if updated_application:
                    res = {'success': True, 'message': 'Application Downloaded Successfully.'}
                else:
                    res = {'success': True, 'message': 'Something Went Wrong! Please Try Again.'}
        else:
            res = {'success': False, 'message': 'Admin cannot download Apps.'}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def get_user_data(email):
    res = {}
    try:
        user = User.objects.filter(Email = email)
        if len(user) == 1 and user[0].Admin == False:
            downloaded_applications = Applications.objects.filter(Screenshots__has_key=str(user[0].id))
            downloaded_applications = application_serializer(downloaded_applications)
            total_points = 0
            for application in downloaded_applications:
                total_points += application['points']
            total_applications = Applications.objects.count()
            profile_data = {
                'downloaded_applications': len(downloaded_applications),
                'total_applications': total_applications,
                'points_earned': total_points
            }
            res = {'success': True, 'profile_data': profile_data}
        else:
            res = {'success': False, 'message':'Something went wrong. Please Try Again!'}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def get_completed_tasks(email):
    res = {}
    try:
        user = User.objects.filter(Email = email)
        if len(user) == 1 and user[0].Admin == False:
            downloaded_applications = Applications.objects.filter(Screenshots__has_key=str(user[0].id))
            downloaded_applications = application_serializer(downloaded_applications)
            res = {'success': True, 'completed_tasks': downloaded_applications}
        else:
            res = {'success':False, 'message': 'Tasks are not assigned to admin.'}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res

def get_remaining_tasks(email):
    res = {}
    try:
        user = User.objects.filter(Email=email)
        if len(user) == 1 and user[0].Admin == False:
            remaining_applications = Applications.objects.exclude(Screenshots__has_key= str(user[0].id))
            remaining_applications = application_serializer(remaining_applications)
            res = {'success': True, 'remaining_tasks': remaining_applications}
        else:
            res = {'success':False, 'message': 'Tasks are not assigned to admin.'}
    except:
        res = {'success': False, 'message': 'Something went wrong. Please Try Again!'}
    return res
