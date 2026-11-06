"""Schematic of Venetian Expo, Level 2, Halls A-D around booth 55630 (CES 2027).

Our own drawing, not a copy of the Freeman plan. Coordinates are in units of the CTA/Freeman
floor plan "Venetian Expo Halls A-D", revision 10/5/2026 (PDF points on the rotated page,
1 unit = about 0.416 m, checked on a 50 ft booth = 36.6 units). No exhibitor names on purpose
(CES contract section 37c and plain courtesy): booths are anonymous grey blocks.

Re-check every point against the final floor plan in December before launch (TODO.md).
"""

M_PER_UNIT = 0.416

# visible window of the map: x, y, w, h
VIEW = (500, 352, 410, 364)
# narrow screens: the camera may look a bit further north than the desktop window
CAM_BOUNDS = (500, 330, 410, 386)

HALL = [(500, 330), (910, 330), (910, 476), (716, 476), (716, 487), (696, 487), (696, 624),
        (597, 624), (560, 630), (500, 604)]

# public walkways outside the halls: west concourse, corridor to Hall D, Venetian Foyer
WALKWAY = [(500, 608), (559, 634), (598, 628), (698, 628), (698, 505), (709, 505), (709, 662),
           (910, 662), (910, 680), (879, 680), (879, 712), (803, 712), (803, 680), (660, 680),
           (600, 672), (500, 654)]

# openings that join walkway and hall
DOORS = {
    "hall-d": [(698, 487), (716, 487), (716, 505), (698, 505)],
    "hall-c": [(560, 630), (597, 624), (598, 628), (559, 634)],
}

HEALTH = [(560, 337.8), (910, 337.8), (910, 448), (734.5, 448), (734.5, 477.3), (696, 477.3),
          (696, 617.5), (597.5, 617.5), (597.5, 557.5), (500, 557.5), (500, 449), (560, 449)]

BALLROOM = (712, 505, 198, 154)

HEALTH_HUB = (640, 386.9, 55.1, 58.4)

ESCALATORS = {
    "west": (631, 636, 33, 22),
    "foyer": (844, 688, 24, 18),
}


def _row(y0, y1, spans):
    return [(x0, y0, x1 - x0, y1 - y0) for x0, x1 in spans]


# anonymous booth blocks (x, y, w, h)
BOOTHS = (
    # row 1 (cut by the top edge)
    _row(343, 357.7, [(694.8, 724.2), (731.4, 745.9), (753, 782.1), (789.4, 804), (811.3, 833.3),
                      (840.2, 869.7), (877, 899.1)])
    # row 2
    + _row(364.7, 379.7, [(694.8, 709.5), (716.6, 738.5), (745.7, 782.1), (789.4, 804),
                          (811.3, 833.3), (840.2, 884.1), (891.3, 899.1)])
    # row 3 (the island 55529/55629/55530/55630 is drawn separately)
    + _row(386.9, 401.4, [(701.9, 738.5), (745.7, 760.3), (767.6, 782.1), (840.2, 884.1),
                          (891.3, 899.1)])
    + [(811.3, 386.9, 22, 36.7)]
    # row 4
    + _row(408.9, 423.6, [(701.9, 738.5), (753, 772.6), (782.1, 803.8), (840.2, 884.1),
                          (891.3, 899.1)])
    # row 5, along the main Health aisle
    + _row(430.5, 445.3, [(701.9, 738.5), (753, 772.6), (782.1, 803.8), (811.3, 833.3),
                          (840.2, 862.3), (869.6, 891.3), (898, 910)])
    # north-west of the main aisle
    + [(636, 343, 52, 36.7), (564, 352, 26, 27), (591.5, 365, 30, 14), (564, 386, 70, 60),
       (500, 352, 49, 27), (503, 386, 20, 14), (527, 386, 22, 14), (500, 405, 49, 37)]
    # south of the main aisle, west part of the Health area
    + [(500, 461, 18.5, 19), (500, 490, 18.5, 12.5), (500, 511, 18.5, 14), (500, 532.5, 18.5, 22.5),
       (526.5, 461, 22.5, 19), (526.5, 490, 22.5, 12.5), (526.5, 511, 22.5, 14),
       (526.5, 532.5, 22.5, 22.5),
       (564, 461, 11, 19), (564, 486, 11, 54), (564, 547, 11, 14),
       (585, 461, 15, 14), (603, 461, 15.5, 14), (585, 477, 15, 14), (603, 477, 15.5, 14),
       (585, 502.5, 33.5, 30), (585, 537.5, 37.5, 25), (600, 585, 36, 37.5),
       (636, 461, 22, 20), (636, 489, 22, 13.5), (636, 511, 22, 21.5), (636, 536, 22, 13.5),
       (636, 554, 22, 13.5),
       (666.5, 461, 14.5, 20), (666.5, 489, 14.5, 13.5), (666.5, 511, 14.5, 14),
       (666.5, 532.5, 14.5, 13.5), (666.5, 554, 14.5, 13.5),
       (644, 577.5, 15, 16), (666, 577.5, 15, 16), (644, 597, 15, 15.5), (666, 597, 15, 15.5),
       (687.5, 480, 7.5, 12), (687.5, 494, 7.5, 12), (687.5, 508, 7.5, 12), (687.5, 522, 7.5, 12),
       (687.5, 536, 7.5, 12),
       (687.7, 460, 21.6, 13.9), (717.1, 460, 14.4, 13.9)]
)

# island: three neighbours + ours (NE corner, open on two sides)
ISLAND_OTHERS = [(789.4, 386.9, 7.3, 7.3), (789.4, 394.2, 7.3, 7.2), (796.7, 394.2, 7.3, 7.2)]
OUR_BOOTH = (796.7, 386.9, 7.3, 7.3)
OUR_BOOTH_CENTER = (800.35, 390.55)

LABELS = [
    # text, x, y, kind
    ("Venetian Ballroom", 811, 586, "area"),
    ("Venetian Foyer", 760, 677.5, "walk"),
    ("West concourse", 503, 641, "walkl"),
    ("Health Hub", 667.5, 419, "hub"),
    ("HEALTH", 520, 470, "zone"),
    ("Main Health aisle", 846, 455.6, "aisle"),
]

ENTRANCES = {
    "hall-d": {"label": "Hall D entrance", "door": (707, 487), "label_at": (720, 497), "anchor": "start"},
    "hall-c": {"label": "Hall C entrance", "door": (578, 627), "label_at": (584, 638), "anchor": "start"},
}

ESCALATOR_LABELS = [
    ("Escalators to Level 1", 647.5, 670, "middle"),
    ("Escalators", 838, 700, "end"),
]

ROUTES = {
    "foyer": {
        "tab": "From the Venetian Foyer",
        "short": "Venetian Foyer",
        "points": [(856, 690), (856, 667.5), (703.5, 667.5), (703.5, 496), (713.2, 483), (713.2, 452.6),
                   (807.6, 452.6), (807.6, 393)],
        # index of the vertex where each step ENDS
        "step_ends": [2, 3, 5, 6, 7],
        "steps": [
            "Leave the escalators and walk along the Venetian Ballroom, keeping it on your right.",
            "At the end of the ballroom, turn right into the corridor to the Hall D entrance.",
            "Go through the Hall D entrance and straight on to the main Health aisle.",
            "Turn right and walk about 40 m, then turn left into a narrow aisle.",
            "Booth 55630 is about 25 m ahead on your left, at the corner.",
        ],
        "meta": "About 230 m from the escalators, 3-4 minutes on foot",
    },
    "west": {
        "tab": "From the west concourse",
        "short": "West concourse",
        "points": [(566, 646), (577, 628), (580, 576), (580, 452.6), (807.6, 452.6), (807.6, 393)],
        "step_ends": [1, 3, 4, 5],
        "steps": [
            "Walk along the west concourse to the Hall C entrance.",
            "Go through the Hall C entrance and follow the aisle to the main Health aisle.",
            "Turn right, pass the Health Hub and keep going about 95 m. Turn left into a narrow aisle.",
            "Booth 55630 is about 25 m ahead on your left, at the corner.",
        ],
        "meta": "About 200 m from the Hall C entrance, about 3 minutes on foot",
    },
}


def route_length(points):
    import math
    return sum(math.dist(points[i], points[i + 1]) for i in range(len(points) - 1))


if __name__ == "__main__":
    for k, r in ROUTES.items():
        L = route_length(r["points"])
        print(k, round(L, 1), "units =", round(L * M_PER_UNIT), "m")
