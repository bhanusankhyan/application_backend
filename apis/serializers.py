from .utils import binary_to_str, str_to_binary

def user_data_serializer(new_user):
    user = {
        'name': new_user.Name,
        'email': new_user.Email,
        'admin': new_user.Admin,
        'profile_picture': binary_to_str(new_user.Profile_Picture)
    }
    return user

def categories_serializer(categories):
    new_categories = []
    for category in categories:
        new_categories.append({
            'category_id': category.id,
            'category_name': category.Category_Name
        })
    return new_categories

def sub_categories_serializer(sub_categories):
    new_sub_categories = []
    for sub_category in sub_categories:
        # print(sub_category.__dict__)
        new_sub_categories.append({
            'subcategory_id': sub_category.id,
            'subcategory_name': sub_category.SubCategory_Name
        })
    return new_sub_categories

def application_serializer(application):
    new_application = []
    for app in application:
        new_app = {
        'app_id': app.id,
        'app_name': app.App_Name,
        'app_link': app.App_link,
        'description': app.Description,
        'points': app.Points,
        'app_image': binary_to_str(app.Application_Picture),
        }
        new_application.append(new_app)
    return new_application
