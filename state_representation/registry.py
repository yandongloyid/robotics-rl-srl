from state_representation import SRLType
from environments.kuka_gym.kuka_button_gym_env import KukaButtonGymEnv

# format NAME: (SRLType, LIMITED_TO_ENV)
registered_srl = {
    "raw_pixels": (SRLType.ENVIRONMENT, None),
    "ground_truth": (SRLType.ENVIRONMENT, None),
    "joints": (SRLType.ENVIRONMENT, [KukaButtonGymEnv]),
    "joints_position": (SRLType.ENVIRONMENT, [KukaButtonGymEnv]),
    "robotic_priors": (SRLType.SRL, None),
    "inverse": (SRLType.SRL, None),
    "forward": (SRLType.SRL, None),
    "multi_view_srl": (SRLType.SRL, None),
    "srl_combination": (SRLType.SRL, None),
    "supervised": (SRLType.SRL, None),
    "autoencoder": (SRLType.SRL, None),
    "autoencoder_inverse": (SRLType.SRL, None),
    "autoencoder_reward": (SRLType.SRL, None),
    "autoencoder_forward": (SRLType.SRL, None),
    "random": (SRLType.SRL, None),
    "random_inverse": (SRLType.SRL, None),
    "reward_inverse": (SRLType.SRL, None),
    "srl_splits": (SRLType.SRL, None),
    "srl_split_forward": (SRLType.SRL, None),
    "srl_3_splits": (SRLType.SRL, None),
    "reward": (SRLType.SRL, None),
    "vae": (SRLType.SRL, None),
    "dae": (SRLType.SRL, None),
    "pca": (SRLType.SRL, None)
}
