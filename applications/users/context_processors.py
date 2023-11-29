def important(request):
    context =  dict()
    context['company'] = 'PoolMasters'
    context['email'] = 'info@poolmasters.co.za'
    context['email2'] = 'carrie@poolmasters.co.za'
    context['tel1'] = '+27 67 735 2242'
    context['tel2'] = '+27 63 859 9481'
    return context