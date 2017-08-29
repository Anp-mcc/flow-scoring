from scoring.StudyService import StudyService
import getopt
import sys


def main(argv):
    config_path = ''
    input_file = ''
    scoring_path = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:c:s:", ["ifile=", "cfile=", "sfile="])
    except getopt.GetoptError as ge:
        print("run -i <inputfile> -c <configfile>")
        print("Getopt error({0})".format(ge))
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("-i <inputfile> -c <configfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-c", "--cfile"):
            config_path = arg
        elif opt in ("-s", "--sfile"):
            scoring_path = arg

    if config_path is not '' and input_file is not '' and scoring_path is not '':
        StudyService.run_study(input_file, scoring_path, config_path)

if __name__ == "__main__":
    main(sys.argv[1:])
