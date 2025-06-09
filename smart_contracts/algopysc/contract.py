from algopy import ARC4Contract, method, GlobalState, LocalState, UInt8, String, itxn

class MarketApp(ARC4Contract):
    class global_state(GlobalState):
        farmer_count: UInt8
        buyer_count: UInt8