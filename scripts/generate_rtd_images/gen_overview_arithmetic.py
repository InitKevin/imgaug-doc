from __future__ import print_function, division

import imgaug as ia
import imgaug.augmenters as iaa

from .utils import run_and_save_augseq


def main():
    chapter_augmenters_add()
    chapter_augmenters_addelementwise()
    chapter_augmenters_additivegaussiannoise()
    chapter_augmenters_additivelaplacenoise()
    chapter_augmenters_multiply()
    chapter_augmenters_multiplyelementwise()
    chapter_augmenters_dropout()
    chapter_augmenters_coarsedropout()
    chapter_augmenters_invert()
    chapter_augmenters_contrastnormalization()


def chapter_augmenters_add():
    aug = iaa.Add((-40, 40))
    run_and_save_augseq(
        "arithmetic/add.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2
    )

    aug = iaa.Add((-40, 40), per_channel=0.5)
    run_and_save_augseq(
        "arithmetic/add_per_channel.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2)


def chapter_augmenters_addelementwise():
    aug = iaa.AddElementwise((-40, 40))
    run_and_save_augseq(
        "arithmetic/addelementwise.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=90
    )

    aug = iaa.AddElementwise((-40, 40), per_channel=0.5)
    run_and_save_augseq(
        "arithmetic/addelementwise_per_channel.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=90
    )


def chapter_augmenters_additivegaussiannoise():
    aug = iaa.AdditiveGaussianNoise(scale=(0, 0.2*255))
    run_and_save_augseq(
        "arithmetic/additivegaussiannoise.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2,
        quality=90
    )

    aug = iaa.AdditiveGaussianNoise(scale=0.2*255)
    run_and_save_augseq(
        "arithmetic/additivegaussiannoise_large.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=90
    )

    aug = iaa.AdditiveGaussianNoise(scale=0.2*255, per_channel=True)
    run_and_save_augseq(
        "arithmetic/additivegaussiannoise_per_channel.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=90
    )


def chapter_augmenters_additivelaplacenoise():
    aug_cls = iaa.AdditiveLaplaceNoise
    fn_start = "arithmetic/additivelaplacenoise"

    aug = aug_cls(scale=(0, 0.2*255))
    run_and_save_augseq(
        fn_start + ".jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2,
        quality=95
    )

    aug = aug_cls(scale=0.2*255)
    run_and_save_augseq(
        fn_start + "_large.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=95
    )

    aug = aug_cls(scale=0.2*255, per_channel=True)
    run_and_save_augseq(
        fn_start + "_per_channel.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=95
    )


def chapter_augmenters_multiply():
    aug = iaa.Multiply((0.5, 1.5))
    run_and_save_augseq(
        "arithmetic/multiply.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(16)], cols=8, rows=2
    )

    aug = iaa.Multiply((0.5, 1.5), per_channel=0.5)
    run_and_save_augseq(
        "arithmetic/multiply_per_channel.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(16)], cols=8, rows=2
    )


def chapter_augmenters_multiplyelementwise():
    aug = iaa.MultiplyElementwise((0.5, 1.5))
    run_and_save_augseq(
        "arithmetic/multiplyelementwise.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=90
    )

    aug = iaa.MultiplyElementwise((0.5, 1.5), per_channel=True)
    run_and_save_augseq(
        "arithmetic/multiplyelementwise_per_channel.jpg", aug,
        [ia.quokka(size=(512, 512)) for _ in range(1)], cols=1, rows=1,
        quality=90
    )


def chapter_augmenters_dropout():
    aug = iaa.Dropout(p=(0, 0.2))
    run_and_save_augseq(
        "arithmetic/dropout.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2)

    aug = iaa.Dropout(p=(0, 0.2), per_channel=0.5)
    run_and_save_augseq(
        "arithmetic/dropout_per_channel.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2)


def chapter_augmenters_coarsedropout():
    aug = iaa.CoarseDropout(0.02, size_percent=0.5)
    run_and_save_augseq(
        "arithmetic/coarsedropout.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2)

    aug = iaa.CoarseDropout((0.0, 0.05), size_percent=(0.02, 0.25))
    run_and_save_augseq(
        "arithmetic/coarsedropout_both_uniform.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2,
        seed=2
    )

    aug = iaa.CoarseDropout(0.02, size_percent=0.15, per_channel=0.5)
    run_and_save_augseq(
        "arithmetic/coarsedropout_per_channel.jpg", aug,
        [ia.quokka(size=(128, 128)) for _ in range(8)], cols=4, rows=2,
        seed=2
    )


def chapter_augmenters_invert():
    aug = iaa.Invert(0.5)
    run_and_save_augseq(
        "arithmetic/invert.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(16)], cols=8, rows=2
    )

    aug = iaa.Invert(0.25, per_channel=0.5)
    run_and_save_augseq(
        "arithmetic/invert_per_channel.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(16)], cols=8, rows=2
    )


def chapter_augmenters_contrastnormalization():
    aug = iaa.ContrastNormalization((0.5, 1.5))
    run_and_save_augseq(
        "arithmetic/contrastnormalization.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(16)], cols=8, rows=2
    )

    aug = iaa.ContrastNormalization((0.5, 1.5), per_channel=0.5)
    run_and_save_augseq(
        "arithmetic/contrastnormalization_per_channel.jpg", aug,
        [ia.quokka(size=(64, 64)) for _ in range(16)], cols=8, rows=2
    )


if __name__ == "__main__":
    main()
