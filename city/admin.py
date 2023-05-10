from django.contrib import admin

from city.models import Category, CityObjects, CityName


@admin.register(CityName)
class CityNameAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CityObjects)
class CityObjectAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "city")


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):

#     list_display = ("id", "title", "author", "cover_type", "publish_year", "my_categories", "my_field")
#     list_filter = ("publish_year", "cover_type")
#     search_fields = ("title", "author")
#     list_display_links = ("id", "title")
#     list_per_page = 10
#     date_hierarchy = "create_time"

#     def my_categories(self, instance):
#         return ", ".join([i[0] for i in instance.categories.all().values_list("title")])
#         # return ", ".join([i.title for i in instance.categories.all()])
#     my_categories.short_description = "Категории"

#     def my_field(self, instance):
#         return f"Hello {instance.publish_year}"
#     my_field.short_description = "Кастомное поле"
