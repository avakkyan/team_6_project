import { motion } from 'framer-motion'
import React from 'react'
import PickedSkill from './PickedSkill'
import { GradeType, SkillType } from '../dashboards/RecruitmentDashboard'
import { GradesToLevelMap } from '../../lib/data'

const PickedSKillsDisplay = ({ pickedSkills, setPickedSkills }: { pickedSkills: SkillType[], setPickedSkills: React.Dispatch<React.SetStateAction<SkillType[]>> }) => {
    return (
        <motion.div
            className='flex gap-2 flex-wrap w-full'>
            {pickedSkills.map((skill) => {
                return (
                    <PickedSkill
                        skill={skill}
                        onClick={() => setPickedSkills((prev) => prev.filter(item => item !== skill))}
                        updateGrade={(skill: string, grade: GradeType) => {
                            setPickedSkills((prev) => {
                                return prev.map((pickedSkill) => ({ name: pickedSkill.name, level: pickedSkill.name == skill ? GradesToLevelMap.get(grade) : pickedSkill.level }))
                            })
                        }}
                    />
                )
            })}
        </motion.div>
    )
}

export default PickedSKillsDisplay