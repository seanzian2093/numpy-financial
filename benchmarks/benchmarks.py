from decimal import Decimal

import numpy as np

import numpy_financial as npf


class Npv2D:

    param_names = ["n_cashflows", "cashflow_lengths", "rates_lengths"]
    params = [
        (1, 10, 100),
        (1, 10, 100),
        (1, 10, 100),
    ]

    def __init__(self):
        self.rates_decimal = None
        self.rates = None
        self.cashflows_decimal = None
        self.cashflows = None

    def setup(self, n_cashflows, cashflow_lengths, rates_lengths):
        rng = np.random.default_rng(0)
        cf_shape = (n_cashflows, cashflow_lengths)
        self.cashflows = rng.standard_normal(cf_shape)
        self.rates = rng.standard_normal(rates_lengths)
        self.cashflows_decimal = rng.standard_normal(cf_shape).astype(Decimal)
        self.rates_decimal = rng.standard_normal(rates_lengths).astype(Decimal)

    def time_broadcast(self, n_cashflows, cashflow_lengths, rates_lengths):
        npf.npv(self.rates, self.cashflows)

    def time_for_loop(self, n_cashflows, cashflow_lengths, rates_lengths):
        for rate in self.rates:
            for cashflow in self.cashflows:
                npf.npv(rate, cashflow)

    def time_broadcast_decimal(self, n_cashflows, cashflow_lengths, rates_lengths):
        npf.npv(self.rates_decimal, self.cashflows_decimal)

    def time_for_loop_decimal(self, n_cashflows, cashflow_lengths, rates_lengths):
        for rate in self.rates_decimal:
            for cashflow in self.cashflows_decimal:
                npf.npv(rate, cashflow)

