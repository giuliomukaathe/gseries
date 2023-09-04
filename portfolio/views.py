from django.shortcuts import render
from .models import PortfolioItem, Category

def portfolio_view(request):
    portfolio_items = PortfolioItem.objects.all()
    categories = Category.objects.all()

    # Get the selected category from the query parameter
    selected_category = request.GET.get('category')

    # Filter items based on the selected category
    if selected_category:
        portfolio_items = portfolio_items.filter(category__name=selected_category)

    context = {'portfolio_items': portfolio_items, 'portfolio_categories': categories}
    return render(request, 'portfolio/portfolio.html', context)
