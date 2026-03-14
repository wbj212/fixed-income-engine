import numpy as np

def calculate_bond_price(face_value, coupon_rate, market_rate, years_to_maturity, frequency=2):
    """Calculates the present value of a bond using semi-annual discounting"""
    periods = years_to_maturity * frequency
    periodic_rate = market_rate / frequency
    coupon_payment = (face_value * coupon_rate) / frequency
    
    # Present value of coupons + face value
    pv_coupons = sum([coupon_payment / (1 + periodic_rate)**t for t in range(1, int(periods) + 1)])
    pv_face = face_value / (1 + periodic_rate)**periods
    return pv_coupons + pv_face

def calculate_duration_convexity(face_value, coupon_rate, market_rate, years_to_maturity, frequency=2):
    """Calculates Modified Duration and Convexity for sensitivity analysis"""
    dt = 0.0001 # Small yield shift for numeric derivative
    p_up = calculate_bond_price(face_value, coupon_rate, market_rate + dt, years_to_maturity, frequency)
    p_down = calculate_bond_price(face_value, coupon_rate, market_rate - dt, years_to_maturity, frequency)
    p_0 = calculate_bond_price(face_value, coupon_rate, market_rate, years_to_maturity, frequency)
    
    # Numeric Duration: (P_down - P_up) / (2 * P_0 * dt)
    mod_duration = (p_down - p_up) / (2 *p_0 *dt)
    # Numeric Convexity: (P_up + P_down - 2*P_0) / (P_0 * dt^2)
    convexity = (p_up + p_down - 2*p_0) / (p_0 *dt**2)
    
    return round(mod_duration,4), round(convexity,4)
