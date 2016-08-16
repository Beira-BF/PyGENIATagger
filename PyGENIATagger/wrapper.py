import subprocess
import os
import logging


class GENIATagger:
    def __init__(self, genia_path):
        self.genia_path = os.path.abspath(genia_path)

    def tag_files(self, files_directory):

        # Find all files
        files_directory = os.path.abspath(files_directory)
        files = os.listdir(files_directory)

        # Create output folder
        output_directory = os.path.abspath(files_directory + '/output')
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # iterate over files
        for f in files:
            file_path = os.path.join(files_directory, f)
            if os.path.isfile(file_path):
                self.tag_file(file_path)
            else:
                logging.warning('{0} is not a file'.format(file_path))

    def tag_file(self, file_path):
        try:
            genia_tagger = subprocess.Popen([self.genia_path, file_path])
            logging.info('Tagger is starting')
            stdout, stderr = genia_tagger.communicate()
            logging.info('Tagger has finished')

            if genia_tagger.returncode < 0:
                logging.error('Tagger call for file {0} '
                              'terminated by signal {1}'
                              .format(file_path, genia_tagger))
            else:
                logging.info('Tagger call for file {0} '
                             'ended with no problems'.format(file_path))

        except OSError as e:
            logging.error('Tagger call for file {0} '
                          'produced an OSError with message\n{1}'
                          .format(file_path, e))


if __name__ == '__main__':
    tagger = GENIATagger('../../geniatagger/geniatagger/')
    tagger.tag_files('data/')
