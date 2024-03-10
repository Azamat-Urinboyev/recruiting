from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DriverForm, CompanyForm
from .models import Driver, Company

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


# Create your views here.

STATES = [
    "Unimportant", 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
    'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
    'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
    'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
    'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
    'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
    'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
    'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
]

RATES_CPM = ["55 CPM", "60 CPM", "65 CPM"]
RATES_PER = ["22-24%", "25%", "27-28%", "30%"]
RATES = RATES_CPM + RATES_PER

AGES = ["Unimportant", "20-23 y.o", "24-30 y.o", "30-40 y.o", "40-50 y.o", "50-55 y.o"]

EXPS = ["Unimportant", "less than a year", "1-2 year", "+2 years"]\

NATIONS = ["Unimportant", "White", "Black", "Latino", "Asian", "SNG"]


def calculate_suitability(company, driver):
    percentage = 0
    flag = True
    try:
        if EXPS.index(company.experience) <= EXPS.index(driver.experience):
            percentage += 20

        if driver.rate in RATES_CPM:
            if RATES_CPM.index(company.rate) >= RATES_CPM.index(driver.rate):
                percentage += 20
                flag = False
        elif driver.rate in RATES_PER and flag:
            if RATES_PER.index(company.rate) >= RATES_PER.index(driver.rate):
                percentage += 20

        if company.nationality == driver.nationality or company.nationality == "Unimportant":
            percentage += 20
        if company.state == driver.state or company.state == "Unimportant":
            percentage += 20
        if AGES.index(company.age) >= AGES.index(driver.age) or company.age == "Unimportant":
            percentage += 20
    except:
        pass

    return percentage


@login_required
def driver_list(request):
    drivers = Driver.objects.all()
    context = {
        "drivers": drivers
    }
    return render(request, "index.html", context)

@login_required
def driver_info(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    companies = Company.objects.all()

    company_progress_list = []
    for company in companies:
        percentage = calculate_suitability(company, driver)
        company_progress_list.append({
            "name": company.name,
            "progress": percentage
        })

    # Sort the list based on the progress percentage
    sorted_company_progress_list = sorted(company_progress_list, key=lambda x: x["progress"], reverse=True)[:5]
    context = {
        "driver": driver,
        "companies": sorted_company_progress_list
    }
    return render(request, "driver-info.html", context)

@login_required
def add_driver(request):
    context = {
            "states": STATES[1:],
            "rates": RATES,
            "ages": AGES[1:],
            "exps": EXPS[1:],
            "nations": NATIONS[1:]
        }
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save()
            return redirect(request.path)
    else:
        form = DriverForm()
        context["form"] = form
    return render(request, "add-driver.html", context)

@login_required
def companies_list(request):
    companies = Company.objects.all()

    context = {
        "companies": companies
    }
    return render(request, "companies.html", context)

@login_required
def company_info(request, company_id):
    company = get_object_or_404(Company, id=company_id)

    rate = []
    if company.rate_cpm != "No option":
        rate.append(company.rate_cpm)
    if company.rate_per != "No option":
        rate.append(company.rate_per)

    rate = " or ".join(rate)

    context = {
        "company": company,
        "rate": rate
    }
    return render(request, "company-info.html", context)

@login_required
def add_company(request):
    context = {
            "states": STATES,
            "rates_cpm": RATES_CPM,
            "rates_per": RATES_PER,
            "ages": AGES,
            "exps": EXPS,
            "nations": NATIONS,
        }
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save()
            return redirect(request.path)
    else:
        form = DriverForm()
        context["form"] = form
    return render(request, "add-company.html", context)
    



class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or self.success_url