"""
Usage:
    from src.printer_ids import VENDORS, MODELS
    from escpos.printer import Usb

    printer = Usb(VENDORS.EPSON, MODELS.TM_T20III)
"""

class VENDORS:
    """USB Vendor IDs"""
    EPSON = 0x04b8
    CANON = 0x04a9
    HP = 0x03f0
    BROTHER = 0x04f9
    ZEBRA = 0x0a5f
    STAR = 0x0519
    CITIZEN = 0x1d90
    BIXOLON = 0x1504


class MODELS:
    """USB Product IDs"""
    # Epson Models
    TM_T20III = 0x0e28
    TM_T88V = 0x0202
    TM_T82 = 0x0e15
    TM_U220 = 0x0001
    TM_T20II = 0x0e1a
    TM_T70 = 0x0e28
    TM_T88IV = 0x0e03
    TM_T88VI = 0x0e28
    
    # Canon Models
    LBP6000 = 0x2737
    PIXMA = 0x1746
    
    # HP Models
    LASERJET = 0x0017
    DESKJET = 0x0004
    
    # Brother Models
    QL700 = 0x2042
    QL800 = 0x209b
    
    # Star Models
    TSP100 = 0x0001
    TSP650 = 0x0015
    
    # Zebra Models
    GK420D = 0x0001
    ZP450 = 0x0019


# Common combinations as tuples
EPSON_TM_T20III = (VENDORS.EPSON, MODELS.TM_T20III)
EPSON_TM_T88V = (VENDORS.EPSON, MODELS.TM_T88V)
EPSON_TM_T82 = (VENDORS.EPSON, MODELS.TM_T82)
