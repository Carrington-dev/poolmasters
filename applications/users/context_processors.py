def important(request):
    context =  dict()
    context['company'] = 'PoolMasters'
    context['email'] = 'info@poolmasters.co.za'
    context['tel1'] = '+27 67 735 2242'
    return context