from django.contrib import admin
from .models import Guest, Cottage, Reservation, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):

    list_display = ('res_id', 'guest', 'cottage', 'check_in_date', 'check_out_date', 'status')
    search_fields = ['guest__user__username', 'cottage__cottage_id']
    list_filter = ('status', 'cottage')
    summernote_fields = ('guest_notes', 'host_notes')


# Register your models here.

admin.site.register(Guest)
admin.site.register(Cottage)
admin.site.register(Review)
