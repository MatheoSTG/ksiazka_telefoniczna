from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Person, PhoneNumber, Email
from django.db.models import ProtectedError
from django.contrib import messages
from django.http import HttpResponseRedirect
from itertools import chain
from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'phonebook/index.html'
    context_object_name = 'all_people'
    paginate_by = 10

    def get_queryset(self):
        return Person.objects.order_by('lastName')

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(IndexView, self).post(self, request, *args, **kwargs)


class SearchView(generic.ListView):
    template_name = 'phonebook/searched.html'
    context_object_name = 'all_people'
    paginate_by = 10

    def get_queryset(self):
        data = self.kwargs['data']
        all_people = Person.objects.filter(Q(firstName__contains=data) | Q(lastName__contains=data))
        all_numbers = PhoneNumber.objects.filter(number__contains=data)
        all_email = Email.objects.filter(email__contains=data)
        if all_numbers:
            all_people = chain(all_people, all_numbers)
        if all_email:
            all_people = chain(all_people, all_email)
        return list(all_people)

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(SearchView, self).post(self, request, *args, **kwargs)


class DetailView(generic.DetailView):
    model = Person
    template_name = 'phonebook/detail.html'

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')

        return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))


class PersonCreate(CreateView):
    model = Person
    fields = ['firstName', 'lastName']

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(PersonCreate, self).post(self, request, *args, **kwargs)


class PersonUpdate(UpdateView):
    model = Person
    fields = ['firstName', 'lastName']

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(PersonUpdate, self).post(self, request, *args, **kwargs)


class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('phonebook:index')

    def delete(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
        except ProtectedError:
            messages.add_message(request, messages.ERROR, 'Nie można usunąć osoby która posiada numer telefonu i/lub email!')
            return HttpResponseRedirect(self.success_url)
        return HttpResponseRedirect(self.success_url)


class PhoneCreate(CreateView):
    model = PhoneNumber
    fields = ['number']

    def form_valid(self, form):
        person = Person.objects.get(id=self.kwargs['pk'])
        form.instance.person = person
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(PhoneCreate, self).post(self, request, *args, **kwargs)


class PhoneUpdate(UpdateView):
    model = PhoneNumber
    fields = ['number']

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(PhoneUpdate, self).post(self, request, *args, **kwargs)


class PhoneDelete(DeleteView):
    model = PhoneNumber
    success_url = reverse_lazy('phonebook:index')


class EmailCreate(CreateView):
    model = Email
    fields = ['email']

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(EmailCreate, self).post(self, request, *args, **kwargs)

    def form_valid(self, form):
        person = Person.objects.get(id=self.kwargs['pk'])
        form.instance.person = person
        return super().form_valid(form)


class EmailUpdate(UpdateView):
    model = Email
    fields = ['email']

    def post(self, request, *args, **kwargs):
        data = request.POST.get('data')
        if data:
            return HttpResponseRedirect(reverse('phonebook:search', kwargs={'data': data}))
        else:
            return super(EmailUpdate, self).post(self, request, *args, **kwargs)


class EmailDelete(DeleteView):
    model = Email
    success_url = reverse_lazy('phonebook:index')


