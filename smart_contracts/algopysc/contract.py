from algopy import *

class MarketApp(ARC4Contract):
    class global_state(GlobalState):
        farmer_count: UInt8
        buyer_count: UInt8
     class local_state(LocalState):
        role: String #'farmer or buyer'#
        phone_no: String
        name: String
        crop_name: String
        crop_quantity: UInt8
    @arc4.abimethod
    def create_account(self,role:string,name:string,phone:string)->None:
        assert role=='farmer' or role=='buyer'
        self.local.phone_no=phone_no
        self.local.name=name
        self.local.role=role
        if role=='farmer'
        self.global.farmer_count+=UInt8(1) #'here farmer count will be increased'#
        else role=='buyer'
        self.global.buyer_count+=UInt8(1) #'here buyer count will be increased'#
    @arc4.abimethod
     def add_crop(self,crop_name:string,quantity:UInt8(1))->None:  
         assert self.local.role=='farmer',"only farmers can add crops"
         self.local.crop_name=crop_name
         self.local.crop_quantity=quantity
    @arc4.abimethod
    def request_crop(self,farmer:address,advance_amount:UInt8)->None:
        assert self.local.role=='buyer',"only buyers can request"
    itxn.payment(
        receiver=farmer,
        amount=advance_amount,
        ).submit()
    