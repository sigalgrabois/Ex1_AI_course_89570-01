# sigal graboys 319009304
'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''
import Astar
import ucs
import IDAstar


# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions
def huristic_function(lat1=0, lon1=0, lat2=0, lon2=0):
    distance = Astar.calculate_distance(lat1, lon1, lat2, lon2)
    return distance / 110


def find_ucs_rout(source, target, use=0):
    path = ucs.ucs_function(source, target, use)
    if use == 0:
        return path
    if use == 1:
        return path


def find_astar_route(source, target, use=0):
    path = Astar.a_star_function(source, target, use)


def find_idastar_route(source, target):
    path = IDAstar.ida_star_function(source, target)
    return path


def dispatch(argv):
    from sys import argv

    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    # from sys import argv
    # dispatch(argv)
    print("found path: ")
    source = 145001
    target = 145018
    ucs_path = find_idastar_route(source, target)
