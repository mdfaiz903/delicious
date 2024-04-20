from django.contrib import admin
from . models import sliderModel,ContactModel,BlogPost,BlogCategory,ReceipePost,ReceipeImage,RecipeContentSection,Ingredient,Feedback
# Register your models here.
class RecipeContentSectionInline(admin.TabularInline):
    model = RecipeContentSection
    extra = 1

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class RecipeImageInline(admin.TabularInline):
    model = ReceipeImage
    extra = 1


@admin.register(ReceipePost)
class RecipePostAdmin(admin.ModelAdmin):
    inlines = [RecipeContentSectionInline, IngredientInline, RecipeImageInline]


admin.site.register(sliderModel)
admin.site.register(ContactModel)
admin.site.register(BlogPost)
admin.site.register(BlogCategory)






admin.site.register(ReceipeImage)
admin.site.register(RecipeContentSection)
admin.site.register(Ingredient)

admin.site.register(Feedback)
