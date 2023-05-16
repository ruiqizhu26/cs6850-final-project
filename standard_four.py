from distribution import Distribution


d = Distribution(['u1v', 'u2v', 'u3v', 'u4v'], [])
d.add_constraint([{'EE': None, 'II': []}], 1)


A_is_u1 = [
    {'EE': ['u1v'], 'II': []},
    {'EE': ['u1v', 'u2v'], 'II': []},
    {'EE': ['u1v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
]

A_is_u2 = [
    {'EE': ['u2v'], 'II': []},
    {'EE': ['u1v', 'u2v'], 'II': []},
    {'EE': ['u2v', 'u3v'], 'II': []},
    {'EE': ['u2v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
]

A_is_u3 = [
    {'EE': ['u3v'], 'II': []},
    {'EE': ['u1v', 'u3v'], 'II': []},
    {'EE': ['u2v', 'u3v'], 'II': []},
    {'EE': ['u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v'], 'II': []},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
]

A_is_u4 = [
    {'EE': ['u4v'], 'II': []},
    {'EE': ['u1v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u4v'], 'II': []},
    {'EE': ['u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u2v', 'u3v', 'u4v'], 'II': []},
    {'EE': ['u1v', 'u2v', 'u3v', 'u4v'], 'II': []},
]


# outcomes that A = {u1} can reach v sum up to 1/2
d.add_constraint(A_is_u1, 1/2)
# outcomes that A = {u2} can reach v sum up to 1/2
d.add_constraint(A_is_u2, 1/2)
# outcomes that A = {u3} can reach v sum up to 1/2
d.add_constraint(A_is_u3, 1/2)
# outcomes that A = {u4} can reach v sum up to 1/2
d.add_constraint(A_is_u4, 1/2)

# outcomes that A = {u1, u2} can reach v sum up to 3/4
d.add_constraint(A_is_u1 + A_is_u2, 3/4)
# outcomes that A = {u1, u3} can reach v sum up to 3/4
d.add_constraint(A_is_u1 + A_is_u3, 3/4)
# outcomes that A = {u1, u4} can reach v sum up to 3/4
d.add_constraint(A_is_u1 + A_is_u4, 3/4)
# outcomes that A = {u2, u3} can reach v sum up to 3/4
d.add_constraint(A_is_u2 + A_is_u3, 3/4)
# outcomes that A = {u2, u4} can reach v sum up to 3/4
d.add_constraint(A_is_u2 + A_is_u4, 3/4)
# outcomes that A = {u3, u4} can reach v sum up to 3/4
d.add_constraint(A_is_u3 + A_is_u4, 3/4)

# outcomes that A = {u1, u2, u3} can reach v sum up to 3/4
d.add_constraint(A_is_u1 + A_is_u2 + A_is_u3, 3/4)
# outcomes that A = {u1, u2, u4} can reach v sum up to 3/4
d.add_constraint(A_is_u1 + A_is_u2 + A_is_u4, 3/4)
# outcomes that A = {u1, u3, u4} can reach v sum up to 3/4
d.add_constraint(A_is_u1 + A_is_u3 + A_is_u4, 3/4)
# outcomes that A = {u2, u3, u4} can reach v sum up to 3/4
d.add_constraint(A_is_u2 + A_is_u3 + A_is_u4, 3/4)

# outcomes that A = {u1, u2, u3, u4} can reach v sum up to 3/4
d.add_constraint(A_is_u1 + A_is_u2 + A_is_u3 + A_is_u4, 3/4)


d.find()