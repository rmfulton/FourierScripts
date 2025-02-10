#include <iostream>
#include <functional>
#include <unordered_map>
#include <vector>

class FormalPowerSeries {
private:
    std::function<double(int)> coefficient_function;
    mutable std::unordered_map<int, double> computed_coeffs; // Cache computed values

public:
    explicit FormalPowerSeries(std::function<double(int)> func)
        : coefficient_function(std::move(func)) {}

    double coefficient(int i) const {
        if (computed_coeffs.find(i) != computed_coeffs.end()) {
            return computed_coeffs[i];
        }
        double coeff = coefficient_function(i);
        computed_coeffs[i] = coeff;
        return coeff;
    }

    // Addition
    FormalPowerSeries operator+(const FormalPowerSeries& other) const {
        return FormalPowerSeries([this, other](int i) {
            return this->coefficient(i) + other.coefficient(i);
        });
    }

    // Subtraction
    FormalPowerSeries operator-(const FormalPowerSeries& other) const {
        return FormalPowerSeries([this, other](int i) {
            return this->coefficient(i) - other.coefficient(i);
        });
    }

    // Multiplication (convolution)
    FormalPowerSeries operator*(const FormalPowerSeries& other) const {
        return FormalPowerSeries([this, other](int i) {
            double sum = 0;
            for (int j = 0; j <= i; ++j) {
                sum += this->coefficient(j) * other.coefficient(i - j);
            }
            return sum;
        });
    }

    // Division (1 / this)
    FormalPowerSeries inverse() const {
        if (coefficient(0) == 0) {
            throw std::invalid_argument("Cannot invert a series with a zero constant term.");
        }
        return FormalPowerSeries([this](int i) {
            double sum = (i == 0) ? 1.0 / coefficient(0) : 0.0;
            for (int j = 1; j <= i; ++j) {
                sum -= coefficient(j) * this->inverse().coefficient(i - j);
            }
            return sum / coefficient(0);
        });
    }

    // Print first N terms
    void print(int N) const {
        for (int i = 0; i < N; ++i) {
            double coeff = coefficient(i);
            if (coeff != 0) {
                std::cout << (i == 0 ? "" : " + ") << coeff << "x^" << i;
            }
        }
        std::cout << std::endl;
    }
};

int main() {
    // Exponential series: e^x = sum x^n / n!
    FormalPowerSeries exp_x([](int n) {
        double fact = 1;
        for (int j = 1; j <= n; ++j) fact *= j;
        return 1.0 / fact;
    });

    // 1 / (e^x - 1)
    FormalPowerSeries inv_exp_x_minus_1 = (exp_x - FormalPowerSeries([](int n) { return (n == 0) ? 1.0 : 0.0; })).inverse();

    // x / (e^x - 1)
    FormalPowerSeries bernoulli_series = FormalPowerSeries([](int n) { return (n == 1) ? 1.0 : 0.0; }) * inv_exp_x_minus_1;

    // Compute first 10 Bernoulli numbers
    std::cout << "Bernoulli Numbers:" << std::endl;
    for (int n = 0; n < 10; ++n) {
        double fact = 1;
        for (int j = 1; j <= n; ++j) fact *= j;
        double Bn = bernoulli_series.coefficient(n) * fact;
        std::cout << "B_" << n << " = " << Bn << std::endl;
    }

    return 0;
}
