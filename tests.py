from unittest import TestCase
import pathlib
import pandas as pd

import b3cotahist


class TestB3Cotahist(TestCase):
    def setUp(self):
        self.samples_dir = pathlib.Path('samples')
        self.sample_zip = self.samples_dir / 'cotahist.ZIP'
        self.sample_txt = self.samples_dir / 'cotahist.TXT'

        self.expected_columns = {
            'TIPO_DE_REGISTRO',
            'DATA_DO_PREGAO',
            'CODIGO_BDI',
            'CODIGO_DE_NEGOCIACAO',
            'TIPO_DE_MERCADO',
            'NOME_DA_EMPRESA',
            'ESPECIFICACAO_DO_PAPEL',
            'PRAZO_EM_DIAS_DO_MERCADO_A_TERMO',
            'MOEDA_DE_REFERENCIA',
            'PRECO_DE_ABERTURA',
            'PRECO_MAXIMO',
            'PRECO_MINIMO',
            'PRECO_MEDIO',
            'PRECO_ULTIMO_NEGOCIO',
            'PRECO_MELHOR_OFERTA_DE_COMPRA',
            'PRECO_MELHOR_OFERTA_DE_VENDAS',
            'NUMERO_DE_NEGOCIOS',
            'QUANTIDADE_NEGOCIADA',
            'VOLUME_TOTAL_NEGOCIADO',
            'PRECO_DE_EXERCICIO',
            'INDICADOR_DE_CORRECAO_DE_PRECOS',
            'DATA_DE_VENCIMENTO',
            'FATOR_DE_COTACAO',
            'PRECO_DE_EXERCICIO_EM_PONTOS',
            'CODIGO_ISIN',
            'NUMERO_DE_DISTRIBUICAO',
        }

    def _validate_dataframe(self, df):
        """Helper method to validate returned dataframe structure"""
        if isinstance(df, pd.DataFrame):
            columns = set(df.columns)

        self.assertEqual(columns, self.expected_columns)
        self.assertGreater(len(df), 0)

    def test_read_zip(self):
        """Test read_zip() method"""
        df_pandas = b3cotahist.read_zip(path=self.sample_zip)
        self.assertIsInstance(df_pandas, pd.DataFrame)
        self._validate_dataframe(df_pandas)

    def test_read_txt(self):
        """Test read_txt() method"""
        df_pandas = b3cotahist.read_txt(path=self.sample_txt)
        self.assertIsInstance(df_pandas, pd.DataFrame)
        self._validate_dataframe(df_pandas)

    def test_read_bytes(self):
        """Test read_bytes() method"""
        with open(self.sample_txt, 'rb') as f:
            sample_bytes = f.read()

        df_pandas = b3cotahist.read_bytes(sample_bytes)
        self.assertIsInstance(df_pandas, pd.DataFrame)
        self._validate_dataframe(df_pandas)

    def test_invalid_txt_path(self):
        """Test invalid txt file path"""
        invalid_path = self.samples_dir / 'invalid.csv'
        with self.assertRaises(ValueError):
            b3cotahist.read_txt(invalid_path)
