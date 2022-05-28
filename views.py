from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Region

def index(request):
    return render(request, './index.html')

def contacts(request):
    html = """
        <h2>Contact with us</h2>
        <strong>Tel: +998 93 577-27-04</strong> <br>
        <strong>Email: <a href="https://mail.google.com/mail/u/2/?pli=1#inbox">Click</a></strong> <br>
        <strong>Telegramm: <a href="https://t.me/backenddeveloper27">Click</a></strong> <br>
    """
    return HttpResponse(html)

def get_cars(request, id=None):
    if request.method == "GET":
        if 'name' in request.GET:
            searched_text = request.GET['name']
            html = ""
            for item in Region.objects():
                if searched_text.lower() in item.name.lower():
                    html += f'<a href={item.id}>{item.name}</a><br>'
            return HttpResponse(html)

    if id is not None:
        reg = Region.get_by_id(id)
        return HttpResponse(reg.name)
    else:
        html = "<a href='/cars/edit/'>Add</a> <br>"
        for item in Region.objects():
            html += f'<a href=edit/?id={item.id}>{item.name}</a><br>'
        return HttpResponse(html)

def get_1(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://mover.uz/watch/CZnm9Nmm?start=105">
        </video><br><br><br>
        <a href="https://car24.uz/wp-content/uploads/2019/11/photo5238192627768210177.jpg">Click here to see picture</a><br>
    """
    return HttpResponse(html)

def get_2(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://youtu.be/PkkV1vLHUvQ">
        </video><br><br><br>
        <a href="https://www.motortrend.com/uploads/2022/01/2022-Bugatti-Chiron-Super-Sport-65.jpg?fit=around%7C875:492">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_3(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://www.motor1.com/news/243209/ferrari-sp38-video/">
        </video><br><br><br>
        <a href="https://cdn.motor1.com/images/mgl/g7Ono/s1/ferrari-sp38.jpg">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_4(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://insideevs.com/reviews/343202/exclusive-tesla-model-3-video-review-from-uks-top-car-buying-brand/">
        </video><br><br><br>
        <a href="https://www.motortrend.com/uploads/sites/5/2020/07/2018-Tesla-Model-3-18.jpg?fit=around%7C875:492">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_5(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://youtu.be/oVauo_O4qV0">
        </video><br><br><br>
        <a href="https://cdn.bmwblog.com/wp-content/uploads/2019/10/BMW-M8-Gran-Coupe-vs-Audi-RS7-Sportback-5-of-14.jpg">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_6(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://www.carsales.com.au/editorial/details/new-lexus-nx-revealed-130457/">
        </video><br><br><br>
        <a href="https://l1-cms-3.images.lexus-europe.com/lexusone/lexeuenv11/2021-lexus-feel-more-responsible-1920x1080_tcm-3154-2413598.jpg">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_7(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://youtu.be/BMRseEVaO-Q">
        </video><br><br><br>
        <a href="https://www.motortrend.com/uploads/sites/5/2021/08/2022-BMW-X6M-Competition-2.jpg">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_8(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://youtu.be/ES2Dfry8s2U">
        </video><br><br><br>
        <a href="https://www.autostrada.uz/wp-content/uploads/2018/12/chevrolet-tracker-narxi-gm-uzbekistan-nachal-prodavat-trekker-v-avtosalonah-v-tashkente-i-v-uzbekistane.jpg">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_9(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://youtu.be/1JB-ba7Gi5U">
        </video><br><br><br>
        <a href="https://cfx-wp-images.imgix.net/2021/11/2022-Kia-K5-AWD.jpg?auto=compress%2Cformat&fit=crop&h=620&ixlib=php-3.3.0&w=930&wpsize=neve-blog&s=18bdf81abfebf6e74ef52ae664eba4db">Click here to see picture</a>
    """
    return HttpResponse(html)

def get_10(self):
    html = """
        <strong>Video is not uploaded yet!</strong><br>
        <video width="320" height="240" controls>
        <source src="https://youtu.be/Nnedfn0uTyY">
        </video><br><br><br>
        <a href="https://www.hyundai.co.kr/image/upload/asset_library/MDA00000000000009261/20272ef9dabd4b9194b00947bde64d39.jpg">Click here to see picture</a>
    """
    return HttpResponse(html)

def edit_cars(request):
    if request.GET:
        id = int(request.GET['id'])
        
        if 'name' in request.GET:
            name = request.GET['name']

            if id == 0:
                car = Region(name)
                car.save()
            else:
                car = Region(name, id)
                car.save()
            return redirect('/cars/')
        else:
            car = Region.get_by_id(id)
            return render(request, 'cars-edit.html', context={'car': car})
    return render(request, 'cars-edit.html', context={'car': ''})

def find_by_name(request, text):
    html = ""
    array = text.split('-')
    for item in Region.objects():
        if item.name in array:
            html += f'<a href={item.id}>{item.name}</a><br>'
    return HttpResponse(html)
