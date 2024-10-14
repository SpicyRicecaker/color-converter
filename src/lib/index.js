// @ts-nocheck
// place files you want to import through the `$lib` alias in this folder.

// Code fully copied from Mike Bostock @ Observable
// https://observablehq.com/@mbostock/lab-and-rgb

// used for conversion from L*A*B* to CIEXYZ (D50 Reference)
function f(t) {
	return t > 6 / 29 ? t ** 3 : 3 * (6 / 29) ** 2 * (t - 4 / 29)
}

// multiplies 3x3 matrix with vector
function matrix_multiply_vector([a, b, c, d, e, f, g, h, i], [x, y, z]) {
	return [a * x + b * y + c * z, d * x + e * y + f * z, g * x + h * y + i * z]
}

const matrix_lrgb_xyzd50 = [
	0.4360747, 0.3850649, 0.1430804, 0.2225045, 0.7168786, 0.0606169, 0.0139322, 0.0971045, 0.7141733
]

const tristimulus_d50 = [
	matrix_lrgb_xyzd50[0] + matrix_lrgb_xyzd50[1] + matrix_lrgb_xyzd50[2],
	matrix_lrgb_xyzd50[3] + matrix_lrgb_xyzd50[4] + matrix_lrgb_xyzd50[5],
	matrix_lrgb_xyzd50[6] + matrix_lrgb_xyzd50[7] + matrix_lrgb_xyzd50[8]
]

// converts from L*A*B* to CIEXYZ (D50 Reference)
function lab_xyzd50([l, a, b]) {
	const fl = (l + 16) / 116
	const fa = a / 500
	const fb = b / 200
	return [
		tristimulus_d50[0] * f(fl + fa),
		tristimulus_d50[1] * f(fl),
		tristimulus_d50[2] * f(fl - fb)
	]
}

// Note sure where this comes from
const matrix_xyzd50_lrgb = [
	3.1338561, -1.6168667, -0.4906146, -0.9787684, 1.9161415, 0.033454, 0.0719453, -0.2289914,
	1.4052427
]

// converts from CIEXYZ (D50 Reference) to LRGB
function xyzd50_lrgb(xyz) {
	return matrix_multiply_vector(matrix_xyzd50_lrgb, xyz)
}

// gamma corrects linear srgb
function lrgb_rgb1(v) {
	return v <= 0.0031308 ? 12.92 * v : 1.055 * v ** (1 / 2.4) - 0.055
}

// gamma corrects linear srgb
function lrgb_rgb([r, g, b]) {
	return [lrgb_rgb1(r), lrgb_rgb1(g), lrgb_rgb1(b)]
}

function lab_rgb(lab) {
	return lrgb_rgb(xyzd50_lrgb(lab_xyzd50(lab)))
}

function rgb_to_hex_string([r, g, b]) {
	return `#${Math.round(r * 255)
		.toString(16)
		.padStart(2, '0')}${Math.round(g * 255)
		.toString(16)
		.padStart(2, '0')}${Math.round(b * 255)
		.toString(16)
		.padStart(2, '0')}`
}

export function lab_hexrgb(lab) {
    // console.log(rgb_to_hex_string(lab_rgb(lab)))
    return rgb_to_hex_string(lab_rgb(lab))
    // return "#FF0000"
}