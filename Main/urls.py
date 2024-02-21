from django.urls import path
from Main import views
from Main import error_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", view=views.home,name="home"),
    path("my-lists/",view=views.my_lists,name="my_lists"),
    path("my-lists/save/<int:saved_id>",view=views.save_list,name="save_list"),
    path("my-lists/create",view=views.create_list,name="create_list"),
    path("my-lists/shared-lists",view=views.shared_lists,name="shared_lists"),
    path("my-lists/delete/<int:id>",view=views.delete_list,name="delete_list"),
    path("my-lists/<int:list_id>/user/remove",view=views.remove_user,name="remove_user"),
    path("my-lists/<int:list_id>/self/remove",view=views.remove_self,name="remove_self"),
    path("my-lists/<int:list_id>/user/add",view=views.add_user,name="add_user"),
    path("my-lists/list/<int:list_id>",view=views.my_list,name="my_list"),
    path("my-lists/list/<int:list_id>/item/create",view=views.create_item,name="create_item"),
    path("my-lists/list/<int:list_id>/item/edit/<int:item_id>",view=views.edit_item,name="edit_item"),
    path("my-lists/list/<int:list_id>/item/delete/<int:item_id>",view=views.delete_item,name="delete_item"),
    path("my-lists/list/<int:list_id>/item/delete/<int:item_id>/<str:done>",view=views.change_state,name="change_state"),
    path("my-lists/<int:list_id>/message/send",view=views.send_message,name="send_message"),
    path("link-to-discord", view=views.link_discord, name="link_discord"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)