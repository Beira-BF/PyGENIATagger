import subprocess
import os
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')


class GENIATagger:
    def __init__(self, genia_path):
        self.genia_path = genia_path

    def tag(self, files_directory):

        # Find all files
        files = os.listdir(files_directory)

        # Create output folder
        output_directory = os.path(files_directory + '/output')
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # iterate over files
        for f in files:
            file_path = os.path.join(files_directory, f)
            if os.path.isfile(file_path):
                self.give_label(output_directory, file_path)
            else:
                logging.warning('{0} is not a file'.format(file_path))

    def give_label(self, output_directory, doc):
        try:
            tagger = subprocess.call("{tagger} {input_file}".format(
                    tagger=self.genia_path, input_file=doc))
            if tagger < 0:
                logging.error('Tagger call for file {0} '
                              'terminated by signal {1}'.format(doc, tagger))
            else:
                logging.info('Tagger call for file {0} '
                             'ended with no problems'.format(doc))
                
        except OSError as e:
            logging.error('Tagger call for file {0} '
                          'produced an OSError with message\n{1}'
                          .format(doc, e))


if __name__ == '__main__':
    file = open('aux.txt', 'r')

    print(file.__next__)