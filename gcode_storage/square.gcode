
G21        ; Set units to millimeters
G90        ; Absolute positioning
G0 Z5      ; Move Z axis up
G0 X0 Y0   ; Move to starting point
G1 Z-2.0 F100 ; Move Z axis down to cutting depth
G1 X10.0 ; Move along X axis
G1 Y10.0 ; Move along Y axis
G1 X0      ; Move back to starting X position
G1 Y0      ; Move back to starting Y position
G0 Z5      ; Move Z axis up
