use criterion::{black_box, criterion_group, criterion_main, Criterion};
use ndarray::{Array2, Array};
use ndarray_rand::RandomExt;
use ndarray_rand::rand_distr::Normal;

fn get_points() -> Array2<f32> {
    let normal = Normal::new(2., 3.).unwrap();
    let points = Array::random((1000, 2), normal);
    return points;
}

criterion_group!(
    benches,
    benchmark_make_cluster,
    benchmark_centroid,
    benchmark_radius_of_gyration,
    benchmark_axis,
    benchmark_discretised_area,
    benchmark_convex_hull
);
criterion_main!(benches);

