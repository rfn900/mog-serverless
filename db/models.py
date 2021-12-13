import datetime


class Commission:

    def set_commission(self, adr, adt, awin):
        adrecord_commission = adr
        adtraction_commission = adt
        awin_commisstion = awin
        commission = {
            "adrecord": adrecord_commission,
            "adtraction": adtraction_commission,
            "awin": awin_commisstion,
            "updated_at": datetime.datetime.now()
        }

        # return jsonify(commission)
        return commission
