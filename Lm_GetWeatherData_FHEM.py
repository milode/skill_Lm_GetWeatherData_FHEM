from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class Lm_GetWeatherData_FHEM(AliceSkill):
	"""
	Author: milode
	Description: Erzählt die aktuellen wettermesswerte
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
