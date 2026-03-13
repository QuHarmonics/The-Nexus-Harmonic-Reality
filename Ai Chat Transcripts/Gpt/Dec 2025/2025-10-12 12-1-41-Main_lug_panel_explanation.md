# Main lug panel explanation

https://chat.openai.com/c/68ebd0de-ec10-832d-8838-a8e03a24fc30

## USER
side quest service panel with main lugs that means i breaker it in the main panel?

## ASSISTANT
Right—the labeling can be confusing, so here’s the quick electrician’s-eye translation:

### “Main-lug only” (MLO) panel  
* **No master disconnect inside.** The line bars land directly on the bus.  
* Because there’s no main breaker, the National Electrical Code treats it as a **sub-panel** the moment it’s downstream from other service equipment.

### What feeds it?  
* You **must** protect those bus bars with an over-current device located upstream.  
* In a typical residence that means you install a **feeder breaker in your service (main) panel** sized to the ampacity of the conductors you’ll pull to the MLO panel.  
  * Example: #4 AWG Cu THHN feeders → 100 A two-pole breaker at the service panel.

### Disconnect rule (NEC 225.33 & 408.36)  
* The MLO panel is allowed as long as it still meets the “six-handle rule” (no more than six throws to kill all power).  
* If the MLO will end up with more than six breakers, you have three common options:  
  1. Use a back-fed breaker in the top spaces and tie it down with retaining hardware (that back-fed breaker now functions as a main).  
  2. Add a separate disconnect switch ahead of the panel.  
  3. Swap to a factory “main-breaker” version of the enclosure.

### Grounding & bonding checklist for the sub-panel
| Item | In service panel | In MLO sub-panel |
|------|------------------|------------------|
| Neutral-to-case bond | **Bonded** | **Isolated** |
| Ground bar | Optional | **Required** (bonded to case) |
| Equipment grounds | Landed on ground bar | Landed on ground bar |
| Neutrals | Landed on neutral bar | On isolated neutral bar |

### Feeder conductors
1. **Hot-hot-neutral-ground** (4-wire feeder) is the modern requirement inside the same building.  
2. **Ground electrode system** is only needed if this sub-panel is in a detached structure.

### Bottom line  
Yes—you “breaker it” in the main panel. Size the breaker and conductors together, run a 4-wire feeder, keep neutrals isolated in the MLO, and you’re good with code. If you’ll exceed six disconnecting means, plan a main disconnect strategy for that sub-panel.

