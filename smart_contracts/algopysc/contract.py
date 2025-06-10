from algopy import ARC4Contract, method, GlobalState, LocalState, UInt8, String, itxn

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
    def create_account(self,role:string,name:string,phone:string):
        assert role=='farmer' or role=='buyer'
        self.local.phone_no=phone_no
        self.local.name=name
        self.local.role=role
        if role=='farmer'
        self.global.farmer_count+=UInt8(1) #'here farmer count will be increased'#
        else role=='buyer'
        self.global.buyer_count+=UInt8(1) #'here buyer count will be increased'#
