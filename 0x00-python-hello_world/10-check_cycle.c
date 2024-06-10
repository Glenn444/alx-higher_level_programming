#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a single linked list has a cycle
 * @list: Pointer to the single linked list
 *
 * Return: 1 if has a cycle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list->next;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
