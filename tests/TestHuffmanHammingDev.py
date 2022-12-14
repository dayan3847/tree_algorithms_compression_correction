import unittest

from tests.TestHuffmanHamming import TestHuffmanHamming


class TestHuffmanHammingDev(TestHuffmanHamming):

    def setUp(self):
        super().setUp()
        # self.verbose = True
        self.file_list = [
            # 'text_alejo_carpentier_los_pasos_perdidos',
            # 'text_carlos_fuentes_aura',
            # 'text_fernando_del_paso_palinuro_de_mexico',
            # 'text_gabriel_garcia_marquez_cien_años_de_soledad',
            # 'text_jorge_ibarguengoitia_estas_ruinas_que_ves',
            # 'text_juan_rulfo_el_llano_en_llamas_cuento',
            # 'text_juan_rulfo_pedro_paramo',
            # 'text_julio_cortazar_rayuela',
            # 'text_mario_vargas_llosa_pantaleon_y_las_visitadoras',
            'text_hello_world',
        ]

    def test_encode(self):
        super().test_encode()

    def test_generate_errors(self):
        super().test_generate_errors()

    def test_decode(self):
        super().test_decode()

    def test_complete(self):
        super().test_complete()


if __name__ == '__main__':
    unittest.main()
