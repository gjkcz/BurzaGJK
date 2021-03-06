from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from itertools import chain

classes = chain(
	(('R{i}.A'.format(i=i), 'R{i}.A'.format(i=i)) for i in range(1, 9)),
	(('{n}.{clas}'.format(n=i, clas=clas), '{n}.{clas}'.format(n=i, clas=clas))
		for i in range(1, 5) for clas in ('A', 'B', 'C')),
)


class User(User):
	def __str__(self):
		return self.username

	class Meta:
		verbose_name = _('uživatel')
		verbose_name_plural = _('uživatelé')

	visited_class = models.CharField(
		max_length=255,
		choices=classes
	)


class Book(models.Model):
	def __str__(self):
		return '{author}: {name}'.format(
			author=self.author,
			name=self.name,
		)

	class Meta:
		verbose_name = _('kniha')
		verbose_name_plural = _('knihy')

	ISBN = models.CharField(
		max_length=255,  # 13char into four parts
	)
	author = models.CharField(
		max_length=255,
	)
	name = models.CharField(
		verbose_name = _('název'),
		max_length=255,
	)
	image = models.ImageField(
		verbose_name = _('obrázek'),
	)
	subject = models.CharField(
		max_length=255,
	)
	# google_books


class AbstractOffer(models.Model):
	class Meta:
		verbose_name = _('abstraktní nabídka')
		verbose_name_plural = _('abstraktní nabídky')

	price = models.IntegerField(
		verbose_name = _('cena'),
		validators = [
			MinValueValidator(0),
		]
		)
	negotiable = models.BooleanField(
		verbose_name = _('smlouvatelné'),)
	active = models.BooleanField()


class Offer(AbstractOffer):
	def __str__(self):
		return 'vendor: {vendor}, book: {book}, price: {price} Kč'.format(
			vendor=self.vendor.username,
			book=self.book.name,
			price=self.price,
		)

	class Meta:
		verbose_name = _('nabídka')
		verbose_name_plural = _('nabídky')

	vendor = models.ForeignKey(
		User,
		related_name='offer',
		on_delete='cascade',
	)
	buyer = models.ManyToManyField(
		User,
		related_name='bit',
		blank=True,
	)
	final_buyer = models.ForeignKey(
		User,
		related_name='purchase',
		blank=True,
		null=True,
		on_delete='cascade',
	)
	book = models.ForeignKey(
		Book,
		verbose_name = _('kniha'),
		on_delete='cascade',
	)
	description = models.CharField(
		verbose_name = _('stav'),
		max_length=255,
		blank=True,
	)
	will_be_active = models.DateField(
		verbose_name = _('k odebrání od'),
		blank=True,
		null=True,
	)
	buyer_complete = models.BooleanField(
		verbose_name = _('Transakce Proběhla'),
		blank=True,
		default=False,
	)
	vendor_complete = models.BooleanField(
		verbose_name = _('Transakce Proběhla'),
		blank=True,
		default=False,
	)
