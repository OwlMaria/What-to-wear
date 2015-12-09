print ('Куда ты идешь сегодня?')
print ('(на прогулку/на работу/на учебу/на тренировку/на торжественное мероприятие)')
place=input ()
print ('Время суток?')
print ('(утро/день/вечер/ночь)')
timeofday=input()
print ('А что с погодой?')
print ('(дождь/снег/сухо)')
weather= input()
print ('Предпочитаешь контраст в одежде?')
print ('(да/нет)')
contrast=input()
print ('Мы уже почти на финишной прямой, только скажи, какой цвет преобладает в твоей одежде сегодня?')
color=input()
print ('А в аксессуарах?')
color_acs=input()

# ответы должны выбираться из выпадающего при нажатии списка,
# то есть не могут не соответствовать ни одному из предложенных вариантов
# кроме преобладающего цвета (по идее он определяется программой, исходя из других предложенных вещей)

if place='на прогулку':
    if contrast='да':
        if weather='дождь':
            if color_acs='розовый': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/rezinovaya-obuv/rezinovye-sapogi-zhenskie/02241110/
            elif color_acs='черный': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/rezinovaya-obuv/rezinovye-sapogi-zhenskie/02224940/
            elif color_acs='белый': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/rezinovaya-obuv/rezinovye-sapogi-zhenskie/02254068/
            elif color_acs='синий': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/polusapogi-polusap_w/polusapogi-zhenskie-demisezonnye/25254094/
        elif weather='сухо':
            if timeofday='утро':
                if color='темно-синий' or color='черный' or color='коричневый' or color='бежевый' or color='светло-коричневый' or color='кремовый' :
                    if color_acs='белый' or color_acs='кремовый' or color_acs='бежевый': #рандом из всего светлого, кроме высоких каблуков
                    elif color_acs='темно-синий' or color_acs='черный' or color_acs='коричневый': #рандом из всех черных, кроме высоких каблуков
                    elif color_acs='красный' or color_acs='розовый': #3 варианта+смесь
                    elif color_acs='синий' or color_acs='голубой': #4 варианта+смесь
                elif color='синий' or color='голубой' or color='красный' or color='розовый':
                    if color_acs='красный' or color_acs='розовый': #3 варианта+смесь+все белые и все черные, кроме высоких каблуков
                    elif color_acs='синий' or color_acs='голубой': #4 варианта+смесь+все белые и все черные, кроме высоких каблуков
                elif color='смесь холодных цветов':#4 варианта синих+все черные и белые, кроме высоких каблуков+смесь
                elif color='смесь теплых цветов':#3 варианта красных+ все белые, кроме высоких каблуков+смесь
            elif timeofday='вечер':
                if color='темно-синий' or color='черный' or color='коричневый' or color='бежевый' or color='светло-коричневый' or color='кремовый' :
                    if color_acs='белый' or color_acs='кремовый' or color_acs='бежевый': #рандом из всего светлого, кроме балеток
                    elif color_acs='темно-синий' or color_acs='черный' or color_acs='коричневый': #рандом из всех черных, кроме балеток
                    elif color_acs='красный' or color_acs='розовый': #2 варианта
                    elif color_acs='синий' or color_acs='голубой': #3 варианта
                elif color='синий' or color='голубой' or color='красный' or color='розовый':
                    if color_acs='красный' or color_acs='розовый': #2 варианта+все белые и все черные, кроме балеток
                    elif color_acs='синий' or color_acs='голубой': #3 варианта+все белые и все черные, кроме балеток
                elif color='смесь холодных цветов':#3 варианта синих+все черные и белые, кроме балеток
                elif color='смесь теплых цветов':#2 варианта красных+ все белые, кроме балеток
            else: 
                if color='темно-синий' or color='черный' or color='коричневый' or color='бежевый' or color='светло-коричневый' or color='кремовый' :
                    if color_acs='белый' or color_acs='кремовый' or color_acs='бежевый': #рандом из всего светлого
                    elif color_acs='темно-синий' or color_acs='черный' or color_acs='коричневый': #рандом из всех черных
                    elif color_acs='красный' or color_acs='розовый': #3 варианта+смесь
                    elif color_acs='синий' or color_acs='голубой': #4 варианта+смесь
                elif color='синий' or color='голубой' or color='красный' or color='розовый':
                    if color_acs='красный' or color_acs='розовый': #3 варианта+смесь+все белые и все черные
                    elif color_acs='синий' or color_acs='голубой': #4 варианта+смесь+все белые и все черные
                elif color='смесь холодных цветов':#4 варианта синих+все черные и белые+смесь
                elif color='смесь теплых цветов':#3 варианта красных+ все белые+смесь
                
    if contrast='нет':
        if weather='дождь':
            if color='розовый': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/rezinovaya-obuv/rezinovye-sapogi-zhenskie/02241110/
            elif color='синий': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/polusapogi-polusap_w/polusapogi-zhenskie-demisezonnye/25254094/
            elif color='черный': #синие и 2 вар-а черных
            elif if color='темно-коричневый': #2 вар-а черных и 3 вар-а коричневых
            elif if color='бежевый' or color='светло-коричневый' or color='кремовый' : #3 вар-а коричневых и 2 светлых
        elif weather='сухо':
            if timeofday='утро': 
                if color='темно-синий' or color='черный' or color='коричневый': #рандом из всех черных, кроме высоких каблуков
                elif color='белый' or color='кремовый' or color='бежевый': #рандом из всех белых, кроме высоких каблуков +смесь
                elif color='красный' or color='розовый': #3 варианта+смесь
                elif color='синий' or color='голубой': #4 варианта+смесь
            elif timeofday='вечер': 
                if color='темно-синий' or color='черный' or color='коричневый': #рандом из всех черных, кроме балеток
                elif color='белый' or color='кремовый' or color='бежевый': #рандом из всех белых, кроме балеток
                elif color='красный' or color='розовый': #2 варианта
                elif color='синий' or color='голубой': #3 варианта
            else: 
                if color='темно-синий' or color='черный' or color='коричневый': #рандом из всех черных
                elif color='белый' or color='кремовый' or color='бежевый': #рандом из всех белых+смесь
                elif color='красный' or color='розовый': #3 варианта+смесь
                elif color='синий' or color='голубой': #4 варианта+смесь
    
elif place='на тренировку':
    if color='черный' or color='серый': # рандом из всех
    elif color='голубой': # рандом из белый, голубой, серый
    elif color='розовый': # рандом из всех\голубой
    elif color='зеленый': # рандом из черный, серый, розовый
    
elif place='на работу' or place='на учебу':
    if contrast='да':
        if color_acs='красный': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/tufli-tufli_w/00814449/
        elif color_acs='черный' or color_acs='белый': #http://robek.ru/product/27292-tufli-calipso-09103zc01kk.htm
    elif contrast='нет':
        if color='белый' or color='кремовый': #http://robek.ru/product/26247-tufli-tofa-1151017.htm
        elif color='черный' or color='серый' or color='темно-синий': # рандом из имеющихся
        elif color='коричневый' or color='бежевый': # рандом из имеющихся
        
elif place='на торжественное мероприятие':
    if contrast='да':
        # рандом из серебряных, золотых, леопардовых, белых, черных
    elif contrast='нет':
        if color='розовый': #http://robek.ru/product/25665-tufli-tofa-1138267.htm
        elif color='желтый': #http://robek.ru/product/25795-tufli-tofa-1138277.htm
        elif color='синий': #http://kari.com/ru/zhenshchinam/zhenskaya-obuv/tufli-tufli_w/00808677/
        elif color='кремовый' or color='телесный' or color='бежевый':
            # рандом из имеющихся
        elif color='черный': # рандом из имеющихся
        elif color='белый': # рандом из имеющихся
