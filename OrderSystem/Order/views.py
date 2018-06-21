from django.shortcuts import render, render_to_response,redirect
from .models import Menu, Order, Ticket


def menu(request):
    menus = Menu.objects.all()
    menu_list = []
    category = request.GET.get('category')
    get_tag = False
    if category is not None:
        menu_list = Menu.objects.filter(category=category)
        get_tag = True
    return render(request, 'menu.html', {'menus': menus,
                                         'menu_list': menu_list,
                                         'get_tag': get_tag})


def display_order(request):
    order_list = Order.objects.all()
    menu_list = []
    if order_list is not None:
        for order in order_list:
            food = Menu.objects.get(id=order.m_id_id)
            menu_list.append(food)
    return render(request, 'order.html', {'menu_list': menu_list,
                                          'order_list': order_list, })


def add_order(request):
    mid = request.GET.get('id')
    old_order = Order.objects.filter(m_id_id=mid).first()
    if old_order is None:
        new_order = Order.objects.create(m_id_id=mid, amount=1)
        new_order.save()
    else:
        old_order.amount += 1
        old_order.save()
    # success_msg = '添加成功！'
    return redirect(display_order)


def remove_order(request):
    mid = request.GET.get('id')
    rm_order = Order.objects.get(m_id_id=mid)
    if rm_order.amount > 1:
        rm_order.amount -= 1
        rm_order.save()
    else:
        rm_order.delete()
    return redirect(display_order)


def submit(request):
    if request.method == 'POST':
        post = request.POST
        tot_price = 0
        orders = Order.objects.all()
        if post is None:
            return redirect(display_order)
        else:
            for order in orders:
                menu = Menu.objects.get(id=order.m_id_id)
                tot_price += menu.price * order.amount
            ticket = Ticket.objects.create(tot_price=tot_price)
            id_list = request.POST.getlist('oid')
            for ID in id_list:
                ticket.o_id.add(ID)
                ticket.save()
            for order in orders:
                order.delete()
            return render(request, 'menu.html')
