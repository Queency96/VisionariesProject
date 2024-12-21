from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request, 'index.html')

def indexTwo(request):
    return render(request, 'index-2.html')

def indexThree(request):
    return render(request, 'index-3.html')

def indexFour(request):
    return render(request, 'index-4.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def blogDetailsAudio(request):
    return render(request, 'blog-details-audio.html')

def blogDetailsImage(request):
    return render(request, 'blog-details-image.html')

def blogDetailsVideo(request):
    return render(request, 'blog-details-video.html')

def blogDetails(request):
    return render(request, 'blog-details.html')

def blogFull2Column(request):
    return render(request, 'blog-full-2-column.html')

def blogFull3Column(request):
    return render(request, 'blog-full-3-column.html')

def blogLeftSidebar2Col(request):
    return render(request, 'blog-left-sidebar-2-col.html')

def blogLeftSidebar(request):
    return render(request, 'blog-left-sidebar.html')

def blogRightSidebar(request):
    return render(request, 'blog-right-sidebar.html')

def cart(request):
    return render(request, 'cart.html')

def checkOut(request):
    return render(request, 'checkout.html')

def compare(request):
    return render(request, 'compare.html')

def contactUs(request):
    return render(request, 'contact-us.html')

def loginRegister(request):
    return render(request, 'login-register.html')

def myAccount(request):
    return render(request, 'my-account.html')

def productDetailsAffiliate(request):
    return render(request, 'product-details-affiliate.html')

def productDetailsBox(request):
    return render(request, 'product-details-box.html')

def productDetailsGroup(request):
    return render(request, 'product-details-group.html')

def productDetailsVariable(request):
    return render(request, 'product-details-variable.html')

def productDetails(request):
    return render(request, 'product-details.html')

def shopGridFull3Col(request):
    return render(request, 'shop-grid-full-3-col.html')

def shopGridFull4Col(request):
    return render(request, 'shop-grid-full-4-col.html')

def shopGridLeftSidebar3Col(request):
    return render(request, 'shop-grid-left-sidebar-3-col.html')

def shopGridLeftSidebar(request):
    return render(request, 'shop-grid-left-sidebar.html')

def shopGridRightSidebar3Col(request):
    return render(request, 'shop-grid-right-sidebar-3-col.html')

def shopGridRightSidebar(request):
    return render(request, 'shop-grid-right-sidebar.html')

def shopListFull(request):
    return render(request, 'shop-list-full.html')

def shopListLeftSidebar(request):
    return render(request, 'shop-list-left-sidebar.html')

def shopListRightSidebar(request):
    return render(request, 'shop-list-right-sidebar.html')

def singleProductGroup(request):
    return render(request, 'single-product-group.html')

def singleProductSale(request):
    return render(request, 'single-product-sale.html')

def singleProduct(request):
    return render(request, 'single-product.html')

def wishlist(request):
    return render(request, 'wishlist.html')

