#!/usr/bin/env python3
from subprocess import call
call(['clear'])
print('Available Errors:\n\n 1. StopIteration\n 2. ArithmeticError\n 3. AssertionError\n 4. AttributeError\n 5. EOFError\n 6. ImportError\n 7. KeyboardInterrupt\n 8. LookupError\n 9. IndexError\n10. KeyError\n11. SyntaxError\n12. IndentationError\n13. SystemError\n')
er = input('What kind of error would you like today? (Enter number): ')
try:
    if er == '1': raise StopIteration
    if er == '2': raise ArithmeticError
    if er == '3': raise AssertionError 
    if er == '4': raise AttributeError
    if er == '5': raise EOFError
    if er == '6': raise ImportError
    if er == '7': raise KeyboardInterrupt
    if er == '8': raise LookupError
    if er == '9': raise IndexError
    if er == '10': raise KeyError
    if er == '11': raise SyntaxError
    if er == '12': raise IndentationError
    if er == '13': raise SystemError
    else: print('\nSorry, that\'s not an option')
except StopIteration: print('\nHere you go, a shiny, new StopIteration error!')
except ArithmeticError: print('\nHere you go, a shiny, new ArithmeticError error!')
except AssertionError: print('\nHere you go, a shiny, new AssertionError error!')
except AttributeError: print('\nHere you go, a shiny, new AttributeError error!')
except EOFError: print('\nHere you go, a shiny, new EOFError error!')
except ImportError: print('\nHere you go, a shiny, new ImportError error!')
except KeyboardInterrupt: print('\nHere you go, a shiny, new KeyboardInterrupt error!')
except IndexError: print('\nHere you go, a shiny, new IndexError error!')
except KeyError: print('\nHere you go, a shiny, new KeyError error!')
except LookupError: print('\nHere you go, a shiny, new LookupError error!')
except IndentationError: print('\nHere you go, a shiny, new IndentationError error!')
except SyntaxError: print('\nHere you go, a shiny, new SyntaxError error!')
except SystemError: print('\nHere you go, a shiny, new SystemError error!')
except: 
    print('\nWow! Wasn\'t expecting that!')
finally: print('\nNow what on Earth did you want that for?\n')
