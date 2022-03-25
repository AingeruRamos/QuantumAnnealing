ls_outs:
	ls -l outputs

cat_outs:
ifeq "$(err)" "0"
	cat outputs/M_$(id).out
else
	cat outputs/M_$(id).err
endif

rm_outs:
	rm outputs/*
exec:
	rm slurm.sbatch
	cp ../slurm slurm.sbatch
	echo priscilla exec python3 $(file) $(args) >> slurm.sbatch
	sbatch slurm.sbatch

