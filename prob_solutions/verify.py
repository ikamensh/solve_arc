from arc import train_set, ArcIOPair, get_train_problem_by_uid

from arc.evaluation import evaluate_agent

from prob_solutions.agent import HardcodedAgent

agent = HardcodedAgent()

result = evaluate_agent(agent, train_set)
print(result)

# for prob in result.correct:
#     print(prob.uid)
#     for i, (pair, answers) in enumerate(zip(prob.test_pairs, result.raw_answers[prob])):
#         pair.plot(title=f"correct_{prob.uid}_{i}")
#         for attempt in answers:
#             ArcIOPair(pair.x, attempt).plot(title=f"attempt_{prob.uid}_{i}")

# from tests.per_prob.test_solves_tgt import solved as supposedly_solved
#
#
# for uid in supposedly_solved:
#     prob = get_train_problem_by_uid(uid)
#     print(prob.uid)
#     for i, (pair, answers) in enumerate(zip(prob.test_pairs, result.raw_answers[prob])):
#         pair.plot(title=f"correct_{prob.uid}_{i}")
#         for attempt in answers:
#             ArcIOPair(pair.x, attempt).plot(title=f"attempt_{prob.uid}_{i}")

# pc = result.partially_correct - result.correct
# for prob in pc:
#     for i, (pair, answers) in enumerate(zip(prob.test_pairs, result.raw_answers[prob])):
#         best_attempt = answers[0]
#         pair.plot(title=f"correct_{prob.uid}_{i}")
#         ArcIOPair(pair.x, best_attempt).plot(title=f"attempt_{prob.uid}_{i}")
#
