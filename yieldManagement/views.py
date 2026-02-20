from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor,WeekDays, MarketPlaceModel, Strategies, ThreShold, RoomTypeYield, CalenderYield, ForecastYield,BudgetYield, OverRide, NoteYield, ReportYield
from datetime import datetime, date

# Create your views here.


def dashboardView(request):
    return render(request, "yield/dashboard.html")

def mainYieldView(request):
    return render(request, "yield/mainyield.html")
def calenderView(request):
    return render(request, "yield/calender.html")

from .booKingApi import bookingRapidApi, bookingRapidApiHotel, bookingRapidApiLocationId
def marketPlaceView(request):
    #MarketPlaceModel.objects.all().delete()
    weekdays = []
    WeekDays.objects.all().delete()
    day = { 0:"Mon", 1:"Tue", 2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat",6:"Sun"}
    weekdays = WeekDays(day0=day[date.weekday(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day}", '%Y-%m-%d').date())],
                    day1 = day[date.weekday(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day+1}", '%Y-%m-%d').date())],
                    day2 = day[date.weekday(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day+2}", '%Y-%m-%d').date())],
                    day3 = day[date.weekday(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day+3}", '%Y-%m-%d').date())],
                    day4 = day[date.weekday(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day+4}", '%Y-%m-%d').date())],
                    day5 = day[date.weekday(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day+5}", '%Y-%m-%d').date())],
                    day6 = day[date.weekday(datetime.strptime(f"{date.today().year}-{date.today().month}-{date.today().day+6}", '%Y-%m-%d').date())])
    weekdays.save()
    weekdays = WeekDays.objects.all()
    if request.method == "POST":
        formid = request.POST.get("fromId")
        print(formid)
        if formid == "delete":
            hotel = request.POST.get("hotel")
            print(hotel)
            MarketPlaceModel.objects.filter(hotel=hotel).delete()
        if formid == "location":
            location = request.POST.get("location")
            print(location)
            try:
               locationId = bookingRapidApiLocationId(location)
               print(location)
               if MarketPlaceModel.objects.filter(locationId= locationId).first() == None:
                    #bookingRapidApi(location=location, locationId=locationId)
                    print("noooo")
                    dataAll = MarketPlaceModel.objects.filter(locationId= locationId)
                    #print(dataAll)
                    hotels = []
                    for h in dataAll:
                        if h.hotelId == None:
                            h.delete()
                        else:
                            hotels.append(h.hotel)
                    hotelSet = set(hotels)
                    for h in hotelSet:
                        chkin = date.today()
                        chkout = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+1}", '%Y-%m-%d').date()
                        HotelMarket = MarketPlaceModel.objects.filter(hotel=h).first()
                        if HotelMarket.CheckIn0 == None:
                            bookingRapidApiHotel(h,chkin=chkin, chkout=chkout)
                        if HotelMarket.CheckIn1 == None:
                            chkin = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+1}", '%Y-%m-%d').date()
                            chkout = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+2}", '%Y-%m-%d').date()
                            bookingRapidApiHotel(h,chkin=chkin, chkout=chkout)
                        print("nooo", "hotelsprice", HotelMarket.CheckIn2)
                        if HotelMarket.CheckIn2 == None:
                            chkin = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+2}", '%Y-%m-%d').date()
                            chkout = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+3}", '%Y-%m-%d').date()
                            bookingRapidApiHotel(h,chkin=chkin, chkout=chkout)
                        if HotelMarket.CheckIn3 == None:
                            chkin = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+3}", '%Y-%m-%d').date()
                            chkout = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+4}", '%Y-%m-%d').date()
                            bookingRapidApiHotel(h,chkin=chkin, chkout=chkout)
                        if HotelMarket.CheckIn4 == None:
                            chkin = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+4}", '%Y-%m-%d').date()
                            chkout = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+5}", '%Y-%m-%d').date()
                            bookingRapidApiHotel(h,chkin=chkin, chkout=chkout)
                        if HotelMarket.CheckIn5 == None:
                            chkin = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+5}", '%Y-%m-%d').date()
                            chkout = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+6}", '%Y-%m-%d').date()
                            bookingRapidApiHotel(h,chkin=chkin, chkout=chkout)
                        if HotelMarket.CheckIn6 == None:
                            chkin = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+6}", '%Y-%m-%d').date()
                            chkout = datetime.strptime(f"{date.today().year}-{date.today().month}-{(date.today().day)+7}", '%Y-%m-%d').date()
                            bookingRapidApiHotel(h,chkin=chkin, chkout=chkout)

                    marketAllPlace = MarketPlaceModel.objects.filter(locationId= locationId)
                    return render(request, "yield/marketplace.html", {"dataAll":marketAllPlace, "weekdays":weekdays})
               else:
                    print("tessss")
                    
                    marketAllPlace = MarketPlaceModel.objects.filter(location= location)
                    for m in marketAllPlace:
                        print(m.hotel, m.hotelId, m.CheckIn0)
                    return render(request, "yield/marketplace.html", {"dataAll":marketAllPlace,"weekdays":weekdays})
                   
            except:
                return render(request, "yield/marketplace.html", {"weekdays":weekdays})
                   
    else:
        print("okkkk")
        return render(request, "yield/marketplace.html",{"weekdays":WeekDays.objects.all()})



def yieldHistoryView(request):
    return render(request, "yield/yieldhistory.html")

def monthlyView(request):
    return render(request, "yield/monthlyyield.html")
def TopView(request):
    return render(request, "yield/top10.html")
def forcastView(request):
    return render(request, "yield/forcasts.html")

def roomTypeView(request):
    return render(request, "yield/roomtype.html")

def dowYoyView(request):
    return render(request, "yield/dowyoy.html")

def settingView(request):
    threshods = ThreShold.objects.all()
    Allstrategies = Strategies.objects.all()
    overrides = OverRide.objects.all()
    roomtypes = RoomTypeYield.objects.all()
    budgets = BudgetYield.objects.all()
    notes = NoteYield.objects.all()
    forecasts = ForecastYield.objects.all()
    cldrs = CalenderYield.objects.all()
    if request.method == "POST":
        day= None
        formId = request.POST.get("form-id")
        delet = request.POST.get("delete")
        if delet == "forecast":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            ForecastYield.objects.filter(id=int(id)).delete()
        if delet == "budget":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            BudgetYield.objects.filter(id=int(id)).delete()
        if delet == "notes":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            NoteYield.objects.filter(id=int(id)).delete()
        if delet == "strategy":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            Strategies.objects.filter(id=int(id)).delete()
        if delet == "threshold":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            ThreShold.objects.filter(id=int(id)).delete()
        if delet == "roomtype":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            RoomTypeYield.objects.filter(id=int(id)).delete()
        if delet == "override":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            OverRide.objects.filter(id=int(id)).delete()
        if delet == "cldr":
            id = request.POST.get("idd")
            print("yesssss------------", id)
            CalenderYield.objects.filter(id=int(id)).delete()
        if formId == "strategy":
            month = request.POST.get("monthstrat")
            weekday = request.POST.get("weekstrat")
            day = request.POST.get("daystrat")
            sold10 = request.POST.get("sold10")
            sold15 = request.POST.get("sold15")
            sold20 = request.POST.get("sold20")
            sold40 = request.POST.get("sold40")
            sold50 = request.POST.get("sold50")
            sold60 = request.POST.get("sold60")
            print(month)
            try:
                if day != None:
                    strategy = Strategies(months=month, weekdays=weekday, days=day, 
                                  sold10=sold10, sold15=sold15, sold20=sold20,
                                  sold40=sold40, sold50=sold50, sold60 = sold60)
                    strategy.save()
                    print(strategy.months, "----------------")
                    Allstrategies = Strategies.objects.all()
                    day = None
                    return render(request, "yield/settings.html", {"DataStrat":Allstrategies})
            except:
                Allstrategies = Strategies.objects.all()
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies})
        elif formId == "threshold":
            monthShold = request.POST.get("monthshold")
            weekShold = request.POST.get("weekshold")
            minShold = request.POST.get("minshold")
            maxShold = request.POST.get("maxshold")
            sellout = request.POST.get("salloutshold")
            try:
                if minShold != None:
                    threshod = ThreShold(month=monthShold, weekday=weekShold, min_price= minShold,
                                 max_price= maxShold, sellout=sellout)
                    threshod.save()
                    threshods = ThreShold.objects.all()
                    minShold = None
                    return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods})
            except:
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies})
           
        elif formId == "override":
            fromOver = request.POST.get("fromOver")
            toOver = request.POST.get("toOver")
            typeOver = request.POST.get("typeOver")
            valueOver = request.POST.get("valueOver")
            try:
                if fromOver != None:
                    override = OverRide(fromDate= fromOver, toDate=toOver,
                                type=typeOver, value= valueOver)
                    override.save()
                    overrides = OverRide.objects.all()
                    fromOver = None
                    return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods, "DataRide":overrides})
            except:
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods, "DataRide":overrides})

        elif formId == "roomtype":
            roomtype = request.POST.get("Inproomtype")
            minRoome = request.POST.get("minRoom")
            maxRoom = request.POST.get("maxRoom")
            typeprice = request.POST.get("typePriceRoom")
            single = request.POST.get("singleRoom")
            double = request.POST.get("doubleRoom")
            triple = request.POST.get("tripleRoom")
            quad = request.POST.get("quadRoom")
            try:
                if minRoome != None:
                    roomtypedata = RoomTypeYield(roomType=roomtype, min_price= minRoome, max_price=maxRoom,
                                         type=typeprice, single=single, double=double,
                                         triple=triple, quad=quad)
                    roomtypedata.save()
                    roomtypes = RoomTypeYield.objects.all()
                    minRoome= None
                    return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods, "DataRide":overrides, "roomData":roomtypes})

            except:
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods, "DataRide":overrides, "roomData":roomtypes})

        elif formId == "note":
            formNote = request.POST.get("formNote")
            toNote = request.POST.get("toNote")
            contentNote = request.POST.get("contentNote")
            try:
                if formNote != None:
                    notedata = NoteYield(fromDate= formNote, toDate= toNote, note=contentNote)
                    notedata.save()
                    notes = NoteYield.objects.all()
                    formNote = None
                    return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,"noteData":notes})
            except:
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,"noteData":notes})
        elif formId == "budget":
            monthBudget = request.POST.get("monthBudget")
            capacitBudget = request.POST.get("capacitBudget")
            indBudget = request.POST.get("IndBudget")
            groupBudget = request.POST.get("GroupBudget")
            allotBudget = request.POST.get("AllotBudget")
            groupTentBudget = request.POST.get("GroupTentBudget")
            allotentBudget = request.POST.get("AllotentBudget")
            try:
                if monthBudget != None:
                    budget = BudgetYield(monthlydate=monthBudget, capacity=capacitBudget,
                                 occInd=indBudget, occGroup= groupBudget, occAllotment=allotBudget,
                                 occGroupTent=groupTentBudget, occAllotmentTent=allotentBudget)
                    budget.save()
                    budgets = BudgetYield.objects.all()
                    monthBudget = None
                    return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets})

            except:
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets})
        elif formId == "forecast":
            monthforecast = request.POST.get("monthforecast")
            capacitforecast = request.POST.get("capacitforecast")
            indforecast = request.POST.get("Indforecast")
            groupforecast = request.POST.get("Groupforecast")
            allotforecast = request.POST.get("Allotforecast")
            groupTentforecast = request.POST.get("GroupTentforecast")
            allotentforecast = request.POST.get("Allotentforecast")
            try:
                if monthforecast != None:
                    forecast = ForecastYield(monthlydate=monthforecast, capacity=capacitforecast,
                                 occInd=indforecast, occGroup= groupforecast, occAllotment=allotforecast,
                                 occGroupTent=groupTentforecast, occAllotmentTent=allotentforecast)
                    forecast.save()
                    forecasts = ForecastYield.objects.all()
                    monthforecast = None
                    return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets, "forecastData":forecasts})

            except:
               return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets, "forecastData":forecasts})
        elif formId == "cldr":
            typecldr = request.POST.get("typecldr")
            fromcldr = request.POST.get("fromcldr")
            tocldr = request.POST.get("tocldr")
            namecldr = request.POST.get("namecldr")
            if typecldr != None:
                caldr = CalenderYield(type=typecldr, fromDate= fromcldr,
                                      toDate= tocldr, name= namecldr)
                caldr.save()
                typecldr = None
                cldrs = CalenderYield.objects.all()
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets, "forecastData":forecasts,
                                                                "Datacldr":cldrs})
            else:
                return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets, "forecastData":forecasts,
                                                                "Datacldr":cldrs})
    
    return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets, "forecastData":forecasts,
                                                                "Datacldr":cldrs})


# delete{}
def settingDelete(request, status, id):
    print(status, id)
    if status == "forecast":
            forecast = ForecastYield.objects.filter(id = int(id))
            forecast.delete()
            print("--------------", forecast)
            threshods = ThreShold.objects.all()
            Allstrategies = Strategies.objects.all()
            overrides = OverRide.objects.all()
            roomtypes = RoomTypeYield.objects.all()
            budgets = BudgetYield.objects.all()
            notes = NoteYield.objects.all()
            forecasts = ForecastYield.objects.all()
            cldrs = CalenderYield.objects.all()
            return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets, "forecastData":forecasts,
                                                                "Datacldr":cldrs})

    else:
            threshods = ThreShold.objects.all()
            Allstrategies = Strategies.objects.all()
            overrides = OverRide.objects.all()
            roomtypes = RoomTypeYield.objects.all()
            budgets = BudgetYield.objects.all()
            notes = NoteYield.objects.all()
            forecasts = ForecastYield.objects.all()
            cldrs = CalenderYield.objects.all()
            return render(request, "yield/settings.html", {"DataStrat":Allstrategies, "DataThreshd":threshods,
                                                                "DataRide":overrides, "roomData":roomtypes,
                                                                "noteData":notes, "budgetData":budgets, "forecastData":forecasts,
                                                                "Datacldr":cldrs})
